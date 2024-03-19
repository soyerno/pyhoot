from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import JSON

from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # Define a relationship with the Pyhoot model
    pyhoots = db.relationship('Pyhoot', backref='owner', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # def __repr__(self):
    #     return '<User %r>' % self.name

class Pyhoot(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(1000))
    questions = db.Column(JSON)
    config = db.Column(JSON)

    def __init__(self, title, owner_id, config, questions):
        self.title = title
        self.owner_id = owner_id
        self.config = config
        self.questions = questions