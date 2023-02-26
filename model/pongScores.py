""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Pong(db.Model):
    __tablename__ = 'pongs'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _user1 = db.Column(db.String(255), unique=False, nullable=False)
    _user2 = db.Column(db.String(255), unique=False, nullable=False)
    _score1 = db.Column(db.String(255), unique=False, nullable=False)
    _score2 = db.Column(db.String(255), unique=False, nullable=False)
    _result1 = db.Column(db.String(255), unique=False, nullable=False)
    _result2 = db.Column(db.String(255), unique=False, nullable=False)
    _scoreDate = db.Column(db.Date)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, user1="none", user2="none", score1='0', score2='0', result1="none", result2="none", scoreDate=date.today()): # variables with self prefix become part of the object, 
        self._user1 = user1
        self._user2 = user2
        self._score1 = score1
        self._score2 = score2
        self._result1 = result1
        self._result2 = result2
        self._scoreDate = scoreDate
    
    # a getter method, extracts email from object
    @property
    def user1(self):
        return self._user1
    
    # a setter function, allows name to be updated after initial object creation
    @user1.setter
    def user1(self, user1):
        self._user1 = user1
        
    @property
    def user2(self):
        return self._user2
    
    # a setter function, allows name to be updated after initial object creation
    @user2.setter
    def user2(self, user2):
        self._user2 = user2
    
    @property
    def score1(self):
        return self._score1
    
    # a setter function, allows name to be updated after initial object creation
    @score1.setter
    def score1(self, score1):
        self._score1 = score1
    
    @property
    def score2(self):
        return self._score2
    
    # a setter function, allows name to be updated after initial object creation
    @score2.setter
    def score2(self, score2):
        self._score2 = score2

    @property
    def result1(self):
        return self._result1
    
    # a setter function, allows name to be updated after initial object creation
    @result1.setter
    def result1(self, result1):
        self._result1 = result1

    @property
    def result2(self):
        return self._result2
    
    # a setter function, allows name to be updated after initial object creation
    @result2.setter
    def result2(self, result2):
        self._result2 = result2
    
    # dob property is returned as string, to avoid unfriendly outcomes
    @property
    def scoreDate(self):
        scoreDate_string = self._scoreDate.strftime('%m-%d-%Y')
        return scoreDate_string
    
    # dob should be have verification for type date
    @scoreDate.setter
    def scoreDate(self, scoreDate):
        self._scoreDate = scoreDate
    
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.make_dict())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, user1="", user2=""):
        """only updates values with length"""
        if len(user1) != 3:
            self.user1 = user1
        if len(user2) != 3:
            self.user2 = user2
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def make_dict(self):
        return {
            "user1": self.user1,
            "user2": self.user2,
            "score1": self.score1,
            "score2": self.score2,
            "result1": self.result1,
            "result2": self.result2,
            "scoreDate": self.scoreDate
        }



"""Database Creation and Testing """


# Builds working data for testing
def initPong():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        u1 = Pong('AAA', 'BBB', '1', '5', 'Loss', 'Win', date(2023, 1, 22))
        u2 = Pong('AAB', 'ABC', '2', '5', 'Loss', 'Win', date(2023, 1, 21))
        u3 = Pong('AAC', 'GHI', '5', '4', 'Win', 'Loss', date(2023, 1, 20))
        u4 = Pong('AAD', 'FGH', '5', '1', 'Win', 'Loss', date(2023, 1, 19))
        u5 = Pong('AAE', 'TYU', '3','5', 'Loss', 'Win', date(2023, 1, 22))

        users = [u1, u2, u3, u4, u5]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error in {user.user1} and/or {user.user2}")
        
