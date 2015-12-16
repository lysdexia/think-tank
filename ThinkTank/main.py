# -*- coding: utf-8 -*-
from flask import Flask, g
from flaskext.couchdbkit import CouchDBKit
from ThinkTank.api.ThinkTank import api
from ThinkTank.Roles import auth_roles
from ThinkTank.Routes import routes
from ThinkTank.Views import couch_views

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["APP_SECRET_KEY"]

# initialize couchdb connection
couchdb = CouchDBKit(app)
views = couch_views(couchdb)

# add authentication roles 
auth = auth_roles(app)

# initialize routes
routes(app, couchdb, views)

# initialize api
api(app)

"""
import datetime
foo = views.User(
        email="foo@bar.com",
        password = "double secret probation",
        role = "user",
        stamp = datetime.datetime.utcnow(),
        member_since = datetime.datetime.utcnow(),
        last_login = datetime.datetime.utcnow(),
        )
foo.save()
"""
