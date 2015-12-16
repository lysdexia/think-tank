# -*- coding: utf-8 -*-

def couch_views(couchdb):

    class Views(object):

        class User(couchdb.Document):
            username = couchdb.StringProperty()
            password = couchdb.StringProperty()
            salt = couchdb.StringProperty()
            role = couchdb.StringProperty()
            created = couchdb.DateTimeProperty()
            modified = couchdb.DateTimeProperty()

        class Post(couchdb.Document):
            subject = couchdb.StringProperty()
            title = couchdb.StringProperty()
            author = couchdb.StringProperty()
            content = couchdb.StringProperty()
            thread = couchdb.StringProperty()
            parent_thread = couchdb.StringProperty()
            stamp = couchdb.DateTimeProperty()
            media = couchdb.ListProperty()

        User.set_db(couchdb.db)
        Post.set_db(couchdb.db)
    return Views()
