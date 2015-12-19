# -*- coding: utf-8 -*-
from flask import Flask, g
from ThinkTank.api.ThinkTank import api
from ThinkTank.Roles import auth_roles
from ThinkTank.Routes import routes
from ThinkTank.Models import db 

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["APP_SECRET_KEY"]

# initialize db on app
db.init_app(app)

# add authentication roles 
auth = auth_roles(app)

# initialize routes
routes(app, db)

# initialize api
api(app, db)
