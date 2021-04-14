"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum

# TODO: Create a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    event = db.relationship(
        'Event', secondary='guest_event_table', back_populates='guests')

# TODO: Create a model called `Event` with the following fields:
# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table

# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)


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
        'Guest', secondary='guest_event_table', back_populates='event')

    type_event = db.Column(db.Enum(event_type))

# TODO: Create a table `guest_event_table` with the following columns:
# - event_id: Integer column (foreign key)
# - guest_id: Integer column (foreign key)


guest_event_table = db.Table('guest_event_table',
                             db.Column('guest_id', db.Integer,
                                       db.ForeignKey('guest.id')),
                             db.Column('event_id', db.Integer,
                                       db.ForeignKey('event.id'))
                             )
