""" database dependencies to support sqliteDB examples """
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class pongScore(db.Model):
    __tablename__ = 'pongScores'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _user1 = db.Column(db.String(255), unique=False, nullable=False)
    _user2 = db.Column(db.String(255), unique=False, nullable=False)
    _score1 = db.Column(db.String(255), unique=False, nullable=False)
    _score2 = db.Column(db.String(255), unique=False, nullable=False)
    _gameResult = db.Column(db.String(255), unique=False, nullable=False)
    _scoreDate = db.Column(db.Date)
    _level = db.Column(db.Integer, primary_key=True)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, user1, user2, score1, score2, gameResult, scoreDate=date.today(), level): # variables with self prefix become part of the object, 
        self._user1 = user1
        self._user2 = user2
        self._score1 = score1
        self._score2 = score2
        self._gameResult = gameResult
        self._scoreDate = scoreDate
        self._level = level
    
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
    def gameResult(self):
        return self._gameResult
    
    # a setter function, allows name to be updated after initial object creation
    @gameResult.setter
    def gameResult(self, gameResult):
        self._gameResult = gameResult

    @property
    def level(self)
        return self._level

    @level.setter
    def level(self, level)
        self._level = level
    
    # dob property is returned as string, to avoid unfriendly outcomes
    @property
    def scoreDate(self):
        scoreDateString = self._scoreDate.strftime('%m-%d-%Y')
        return scoreDateString
    
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
    def update(self, user1="", user2="", gameResult=""):
        """only updates values with length"""
        if len(user1) != 3:
            self.user1 = user1
        if len(user2) != 3:
            self.user2 = user2
        if len(gameResult) > 0:
            self.set_gameResult(gameResult)
            self.set_level += 1
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
            "gameResult": self.gameResult,
            "scoreDate": self.scoreDate
            "level": self.level
        }



"""Database Creation and Testing """


# Builds working data for testing
def initPong():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        u1 = pongScore('AAA', 'BBB', '1', '5', 'BBB wins', date(2023, 1, 22), '10')
        u2 = pongScore('AAB', 'ABC', '2', '5', 'ABC wins', date(2023, 1, 21), '11')
        u3 = pongScore('AAC', 'GHI', '5', '4', 'AAC wins', date(2023, 1, 20), '5')
        u4 = pongScore('AAD', 'FGH', '5', '1', 'AAD wins', date(2023, 1, 19), '7')
        u5 = pongScore('AAE', 'TYU', '3','5', 'TYU wins', date(2023, 1, 22), '12')

        users = [u1, u2, u3, u4, u5]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.user1} and {user.user2}")
        
