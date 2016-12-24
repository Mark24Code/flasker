from datetime import datetime
from app import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    content = db.Column(db.Text())
    created_at = db.Column(db.DateTime())

    def __index__(self, title, content, created_at=None):
        self.title = title
        self.content = content
        if not created_at:
            created_at = datetime.now()
        self.created_at = created_at

    def __repr__(self):
        return '<Blog %r>' % self.title
