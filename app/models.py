from app import db


class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)
