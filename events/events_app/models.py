"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
from datetime import datetime
import enum


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    events_attending = db.relationship(
        'Event', secondary='guest_event_table', back_populates='guests')


class event_type(enum.Enum):
    PARTY = 1
    STUDY = 2
    NETWORKING = 3


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    date_and_time = db.Column(db.DateTime)
    guests = db.relationship(
        'Guest', secondary='guest_event_table', back_populates='events_attending')

    type_event = db.Column(db.Enum(event_type))


guest_event_table = db.Table('guest_event_table',
                             db.Column('guest_id', db.Integer,
                                       db.ForeignKey('guest.id')),
                             db.Column('event_id', db.Integer,
                                       db.ForeignKey('event.id'))
                             )
