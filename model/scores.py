""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import datetime
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

# Create class Score to add a scores table to database
class Score(db.Model):
    # Table name
    __tablename__ = 'scores'

    # Define the columns for the table
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column(db.String(255), unique=False, nullable=False)
    _score = db.Column(db.String(255), unique=False, nullable=False)
    _dos = db.Column(db.Date)

    # Construct the profile for Score
    def __init__(self, username="none", score='0', dos=date.today()): # variables that record the username, score, and date of score(dos)
        self._username = username
        self.score = score
        self._dos = dos
    
    # Getter method
    @property
    def username(self):
        return self._username
    
    # Setter function
    @username.setter
    def username(self, username):
        self._username = username
    
    # Getter method
    @property
    def score(self):
        return self._score
    
    # Setter function
    @score.setter
    def score(self, score):
        self._score = score
    
    # Convert dos to a string
    @property
    def dos(self):
        dos_string = self._dos.strftime('%m-%d-%Y')
        return dos_string
    
    # Setter function
    @dos.setter
    def dos(self, dos):
        self._dos = dos

    # Output content using json dumps
    def __str__(self):
        return json.dumps(self.make_dict())

    # CRUD operations: create, read, update, delete
    # CREATE: returns self and returns None if there is error
    def create(self):
        try:
            # creates a user object from Score(db.Model) class
            db.session.add(self)  # add persists user object onto table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    # UPDATE: updates username and score
    def update(self, username="", score=""):
        """only updates values with length"""
        if len(username) == 3:
            self.username = username
        if len(score) > 0:
            self.score = score
        db.session.commit()
        return self

    # DELETE: removes a user
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    # READ: converts self to dictionary
    # returns a dictionary
    def make_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "score": self.score,
            "dos": self.dos
        }



"""Database Creation and Testing """


# Builds working data for testing
def initScores():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        u1 = Score('AAA', '2', date(2023, 1, 22))
        u2 = Score('AAB', '2', date(2023, 1, 21))
        u3 = Score('AAC', '1', date(2023, 1, 20))
        u4 = Score('AAD', '1', date(2023, 1, 19))
        u5 = Score('AAE', '1', date(2023, 1, 22))

        users = [u1, u2, u3, u4, u5]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.username}")
        
