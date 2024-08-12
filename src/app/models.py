from . import db
from datetime import datetime
from sqlalchemy import event
import random
import string

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, **kwargs):
        super().__init__(name=name, **kwargs)
        self.slug = self.generate_slug(name)

    def generate_slug(self, name):
        slug = name.lower().replace(' ', '-')
        while Event.query.filter_by(slug=slug).first():
            slug = f"{slug}-{''.join(random.choices(string.ascii_lowercase + string.digits, k=4))}"
        return slug

class Availability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    available_times = db.Column(db.Text, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    event = db.relationship('Event', backref=db.backref('availabilities', lazy=True))
