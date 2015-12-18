# -*- coding: utf-8 -*-
# http://www.mongoalchemy.org/
from flask.ext.mongoalchemy import MongoAlchemy
from mongoalchemy.document import Index
def get_views(app):
    db = MongoAlchemy(app)

    class Post(db.Document):
        subject = db.StringField()
        title = db.StringField()
        author = db.StringField()
        content = db.StringField()
        thread = db.StringField()
        stamp = db.DateTimeField()
        media = db.ListField(db.StringField(), default_empty=True)
        subject_index = Index().ascending("subject")
        thread_index = Index().ascending("subject").ascending("thread")

    app.Post = Post
