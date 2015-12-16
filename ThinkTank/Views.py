# -*- coding: utf-8 -*-

def couch_views(couchdb):

    class Views(object):

        class User(couchdb.Document):
            email = couchdb.StringProperty()
            password = couchdb.StringProperty()
            role = couchdb.StringProperty()
            token = couchdb.StringProperty()
            stamp = couchdb.DateTimeProperty()
            member_since = couchdb.DateTimeProperty()
            last_login = couchdb.DateTimeProperty()

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
