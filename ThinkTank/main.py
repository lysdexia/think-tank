# -*- coding: utf-8 -*-
from flask import Flask, g
from ThinkTank.Roles import auth_roles
from ThinkTank.Routes import routes

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["APP_SECRET_KEY"]

# add authentication roles 
auth = auth_roles(app)

# initialize routes
routes(app)
