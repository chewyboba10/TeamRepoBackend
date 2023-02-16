""" database dependencies to support sqliteDB examples """
from datetime import date
import datetime
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class History(db.Model):
    __tablename__ = 'histories'  # table name is plural, class name is singular
    x = datetime.datetime.now()

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column(db.String(255), unique=False, nullable=False)
    _score = db.Column(db.String(255), unique=False, nullable=False)
    _dos = db.Column(db.Date)
    _tos = db.Column(db.String(255), unique=False)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, username, score, dos=date.today(), tos= x.strftime("%X")):
        self._username = username
        self.score = score
        self._dos = dos
        self._tos = tos
    
    # @property
    # a getter method, extracts email from object
    @property
    def username(self):
        return self._username
    
    # a setter function, allows name to be updated after initial object creation
    @username.setter
    def username(self, username):
        self._username = username
        
    @property
    def score(self):
        return self._score
    
    # a setter function, allows name to be updated after initial object creation
    @score.setter
    def score(self, score):
        self._score = score
    
    # dob property is returned as string, to avoid unfriendly outcomes
    @property
    def dos(self):
        dos_string = self._dos.strftime('%m-%d-%Y')
        return dos_string
    
    # dob should be have verification for type date
    @dos.setter
    def dos(self, dos):
        self._dos = dos
    
    @property
    def tos(self):
        return self._tos
    
    @tos.setter
    def tos(self, tos):
        self._tos = tos
    
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

    # CRUD read converts self to dictionary
    # returns dictionary
    def make_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "score": self.score,
            "dos": self.dos,
            "tos": self.tos
        }


"""Database Creation and Testing """


# Builds working data for testing
def initHistories():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        u1 = History('ABC', '12', date(2023, 1, 22),'00:00:01')
        u2 = History('TES', '20', date(2023, 1, 21), '12:12:12')
        u3 = History('MKO', '10', date(2023, 1, 20), '13:13:14')
        u4 = History('HGI', '15', date(2023, 1, 19), '14:14:16')
        u5 = History('FDM', '100', date(2023, 1, 22), '20:20:12')

        users = [u1, u2, u3, u4, u5]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.username}")
            