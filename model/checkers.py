""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Checkers(db.Model):
    __tablename__ = 'checkers'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _uidB = db.Column(db.String(255), unique=False, nullable=False)
    _uidR = db.Column(db.String(255), unique=False, nullable=False)
    _resultB = db.Column(db.String(255), unique=False, nullable=False)
    _resultR = db.Column(db.String(255), unique=False, nullable=False)
    _dogame = db.Column(db.Date)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, uidB="none", resultB="none", uidR="none", resultR="none", dogame=date.today()): # variables with self prefix become part of the object, 
        self._uidB = uidB
        self.resultB = resultB
        self._uidR = uidR
        self._resultR = resultR
        self._dogame = dogame
    
    # a getter method, extracts email from object
    @property
    def uidB(self):
        return self._uidB
    
    # a setter function, allows name to be updated after initial object creation
    @uidB.setter
    def uidB(self, uidB):
        self._uidB = uidB
        
    @property
    def resultB(self):
        return self._resultB
    
    # a setter function, allows name to be updated after initial object creation
    @resultB.setter
    def resultB(self, resultB):
        self._resultB = resultB

    @property
    def uidR(self):
        return self._uidR
    
    # a setter function, allows name to be updated after initial object creation
    @uidR.setter
    def uidR(self, uidR):
        self._uidR = uidR

    @property
    def resultR(self):
        return self._resultR
    
    # a setter function, allows name to be updated after initial object creation
    @resultR.setter
    def resultR(self, resultR):
        self._resultR = resultR
    
    # dob property is returned as string, to avoid unfriendly outcomes
    @property
    def dogame(self):
        dogame_string = self._dogame.strftime('%m-%d-%Y')
        return dogame_string
    
    # dob should be have verification for type date
    @dogame.setter
    def dogame(self, dogame):
        self._dogame = dogame
    
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
    def update(self, uidB="", uidR="", resultR=""):
        """only updates values with length"""
        if len(uidB) != 3:
            self.uidB = uidB
        if len(uidR) != 3:
            self.uidR = uidR
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
            "uidB": self.uidB,
            "resultB": self.resultB,
            "uidR": self.uidR,
            "resultR": self.resultR,
            "dogame": self.dogame
        }



"""Database Creation and Testing """


# Builds working data for testing
def initCheckers():
    with app.app_context():
        """Create database and tables"""
        # db.create_all()
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        u1 = Checkers('AAA', 'Win', 'AAB', 'Loss', date(2023, 2, 16))
        u2 = Checkers('BBB', 'Win', 'BBC', 'Loss', date(2023, 2, 1))
        u3 = Checkers('CCC', 'Loss', 'CCD', 'Win', date(2023, 2, 10))
        u4 = Checkers('DDD', 'Win', 'DDE', 'Loss', date(2023, 2, 14))
        u5 = Checkers('EEE', 'Loss', 'EEF', 'Win', date(2023, 2, 17))

        users = [u1, u2, u3, u4, u5]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.uidB} or {user.uidR}")
        
