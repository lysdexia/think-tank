# -*- coding: utf-8 -*-
# http://www.mongoalchemy.org/
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = "posts"
    post_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(24))
    title = db.Column(db.String(128))
    author = db.Column(db.String(255), db.ForeignKey("User.username"))
    content = db.Column(db.Text())
    thread = db.Column(db.String(64))
    stamp = db.Column(db.DateTime())

class MediaLink(db.Model):
    __tablename__ = "media_links"
    link_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.post_id"))
    link = db.Column(db.String(256))
