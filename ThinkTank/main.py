# -*- coding: utf-8 -*-
from flask import Flask, g
from ThinkTank.api.ThinkTank import api
from ThinkTank.Roles import auth_roles
from ThinkTank.Routes import routes
from ThinkTank.Views import get_views

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["APP_SECRET_KEY"]

# initialize db on app and get some views
get_views(app)

# add authentication roles 
auth = auth_roles(app)

# initialize routes
routes(app)

# initialize api
api(app)


