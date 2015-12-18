# -*- coding: utf-8 -*-
from flask import Flask, g
from flask.ext.mongoalchemy import MongoAlchemy
from ThinkTank.api.ThinkTank import api
from ThinkTank.Roles import auth_roles
from ThinkTank.Routes import routes
from ThinkTank.Views import think_tank_views

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["APP_SECRET_KEY"]

# initialize mongoalchemy
db = MongoAlchemy(app)

# ugly, but consistent
views = think_tank_views(db)

# add authentication roles 
auth = auth_roles(app)

# initialize routes
routes(app, views)

# initialize api
api(app, views)

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
