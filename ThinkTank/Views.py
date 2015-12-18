# -*- coding: utf-8 -*-
# http://www.mongoalchemy.org/
def think_tank_views(db):

    class Views(object):

        class Post(db.document.Document):
            subject = db.fields.StringField()
            title = db.fields.StringField()
            author = db.fields.StringField()
            content = db.fields.StringField()
            thread = db.fields.StringField()
            parent_thread = db.fields.StringField()
            stamp = db.fields.DateTimeField()
            media = db.fields.ListField()

    return Views()
