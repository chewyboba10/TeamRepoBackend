""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class userLevel(db.Model):
    __tablename__ = 'userLevels'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column(db.String(255), unique=True, nullable=False)
    _gameNumber = db.Column(db.String(255), unique=False, nullable=False)
    _dolg = db.Column(db.Date)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, username="none", gameNumber='0', dolg=date.today()): # variables with self prefix become part of the object, 
        self._username = username
        self._gameNumber = gameNumber
        self._dolg = dolg
    
    # a getter method, extracts email from object
    @property
    def username(self):
        return self._username
    
    # a setter function, allows name to be updated after initial object creation
    @username.setter
    def username(self, username):
        self._username = username
        
    @property
    def gameNumber(self):
        return self._gameNumber
    
    # a setter function, allows name to be updated after initial object creation
    @gameNumber.setter
    def gameNumber(self, gameNumber):
        self._gameNumber = gameNumber
    
    # dob property is returned as string, to avoid unfriendly outcomes
    @property
    def dolg(self):
        dolg_string = self._dolg.strftime('%m-%d-%Y')
        return dolg_string
    
    # dob should be have verification for type date
    @dolg.setter
    def dolg(self, dolg):
        self._dolg = dolg
    
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
    def update(self, username="", gameNumber="", dolg=""):
        """only updates values with length"""
        if len(username) > 0:
            self.username = username
        if len(gameNumber) > 0:
            self.set_gameNumber(gameNumber)
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
            "id": self.id,
            "username": self.username,
            "game number": self.gameNumber,
            "dolg": self.dolg
        }



"""Database Creation and Testing """


# Builds working data for testing
def initUserLevels():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        u1 = userLevel('AAA', '12', date(2023, 1, 22))
        u2 = userLevel('AAB', '20', date(2023, 1, 21))
        u3 = userLevel('AAC', '10', date(2023, 1, 20))
        u4 = userLevel('AAD', '15', date(2023, 1, 19))
        u5 = userLevel('AAE', '100', date(2023, 1, 22))

        users = [u1, u2, u3, u4, u5]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.username}")
        
