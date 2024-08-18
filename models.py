from .app import db
from sqlalchemy import DateTime
import datetime


class UserModel(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(250), nullable=True)
    created_At=db.Column(DateTime, default=datetime.datetime.now() )

    def __init__(self, username, password):
        self.username=username
        self.password=password
    
    def __repr__(self):
        return f"{self.username}"
    