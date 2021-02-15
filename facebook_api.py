import os

import requests
from dotenv import load_dotenv
load_dotenv()
from app.models import Page, db

from app import init_app

app2 = init_app()


def me():
    with app2.app_context():
        url = 'https://graph.facebook.com/v9.0/me'
        params = dict(
            fields='page_token,about,description_html,engagement,fan_count,posts{child_attachments,created_time,picture,shares,status_type,full_picture},picture',
            access_token=os.getenv("ACCESS_TOKEN")
        )

        resp = requests.get(url=url, params=params)
        data = resp.json()

        page = Page(
            id=data['id'],
            page_token=data['page_token'],
            about=data['about'],
            engagement_count=data['engagement']['count'],
            engagement_social_sentence=data['engagement']['social_sentence'],
            fan_count=data['fan_count'],
        )
        db.session.add(page)
        db.session.commit()

        pages = Page.query.all()
        print(pages)


if __name__ == '__main__':
    me()
