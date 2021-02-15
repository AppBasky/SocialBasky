import os

import requests
from dotenv import load_dotenv
load_dotenv()
from app.models import Page, db, Post

from app import init_app
import json

app2 = init_app()


def me():
    with app2.app_context():
        template_path = os.path.join(os.path.dirname(__file__), 'storage', 'data.json')
        try:
            with open(template_path) as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            url = 'https://graph.facebook.com/v9.0/me'
            params = dict(
                fields='page_token,about,description_html,engagement,fan_count,posts{child_attachments,created_time,picture,shares,status_type,full_picture},picture',
                access_token=os.getenv("ACCESS_TOKEN")
            )
            resp = requests.get(url=url, params=params)
            data = resp.json()

            with open(template_path, 'w') as outfile:
                json.dump(data, outfile)

        page = Page(
            id=data['id'],
            page_token=data['page_token'],
            about=data['about'],
            engagement_count=data['engagement']['count'],
            engagement_social_sentence=data['engagement']['social_sentence'],
            fan_count=data['fan_count'],
            picture=json.dumps(data['picture']['data'])
        )
        db.session.add(page)
        db.session.commit()

        for p_data in data['posts']['data']:
            post = Post(
                id=p_data['id'],
                picture=p_data['picture'],
                status_type=p_data['status_type'],
                full_picture=p_data['full_picture'],
                page_id=page.id,
            )
            db.session.add(post)
        db.session.commit()

        # query pages
        # pages = Page.query.all()


if __name__ == '__main__':
    me()
