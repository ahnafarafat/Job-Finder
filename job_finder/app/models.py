from app import db
from datetime import datetime

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    company = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.Text)
    posted_on = db.Column(db.DateTime, default=datetime.utcnow)

