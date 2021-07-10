from flask import current_app
from app import db
from datetime import datetime


# ADMIN PAGE models

class Page(db.Model):
    __tablename__ = 'page'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    last_publish_date = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    page_home = db.relationship(
        "PageHome", backref="page", lazy="dynamic")
    page_contact = db.relationship(
        "PageContact", backref="page", lazy="dynamic")
    create_date = db.Column(db.DateTime,default=datetime.utcnow, nullable=False)

    @staticmethod
    def getPage(name):
        return Page.query.filter_by(name=name).first()

    def __repr__(self):
        return '<Page {}>'.format(self.name)


class PageStatus(db.Model):
    __tablename__ = 'page_status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    create_date = db.Column(db.DateTime,default=datetime.utcnow, nullable=False)
    page_home = db.relationship(
        "PageHome", backref="page_status", lazy="dynamic")
    page_contact = db.relationship(
        "PageContact", backref="page_status", lazy="dynamic")

    @staticmethod
    def getStatus(name):
        return PageStatus.query.filter_by(name=name).first()

    def __repr__(self):
        return '<PageStatus {}>'.format(self.name)


# Add your custom page details below
# The two below are just examples
# You also need to create an entry in Page which is like the parent and will be used by Dashboard

class PageHome(db.Model):
    __tablename__ = 'page_home'
    id = db.Column(db.Integer, primary_key=True)
    hero = db.Column(db.String(100))
    section1 = db.Column(db.String(1000))
    section2 = db.Column(db.String(1000))
    status_id = db.Column(db.Integer, db.ForeignKey('page_status.id'), nullable=False)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    update_date = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    create_date = db.Column(db.DateTime,default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<PageHome {}'.format(self.id)


class PageContact(db.Model):
    __tablename__ = 'page_contact'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    status_id = db.Column(db.Integer, db.ForeignKey('page_status.id'), nullable=False)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    update_date = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    create_date = db.Column(db.DateTime,default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<PageContact {}'.format(self.id)


