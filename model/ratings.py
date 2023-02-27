import datetime
from datetime import date
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key = True)
    _username = db.Column(db.String(255), unique=False, nullable=False)
    _rating = db.Column(db.String(255), unique=False, nullable=False)


    def __init__(self, username="none", rating="none"):
        self._username = username
        self._rating = rating

    @property 
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username 

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    def __str__(self):
        return json.dumps(self.make_dict())

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    def make_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "rating": self.rating
        }
    
    def update(self, username="", rating=""):
        """only updates values with length"""
        if len(username) == 3:
            self.username = username
        if len(rating) > 0:
            self.rating = rating
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

def initRatings():
    with app.app_context():
        db.create_all()

        u1 = Rating('ABC', '1')
        u2 = Rating('JJK', '2')
        u3 = Rating('TES', '3')
        u4 = Rating('QHF', '4')
        u5 = Rating('IWO', '5')

        users = [u1, u2, u3, u4, u5]
        for user in users:
            try:
                user.create()
            except IntegrityError:
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.username}")