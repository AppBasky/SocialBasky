from app import db


class Page(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'pages'
    id = db.Column(
        db.String(128),
        primary_key=True
    )
    page_token = db.Column(
        db.String(128),
        nullable=False,
        default=''
    )
    about = db.Column(
        db.Text,
    )
    engagement_count = db.Column(
        db.Integer,
        default=0
    )
    engagement_social_sentence = db.Column(
        db.String(128),
        default=''
    )
    fan_count = db.Column(
        db.Integer,
        default=0
    )

    def __repr__(self):
        return '<Pages {}>'.format(self.page_token)
