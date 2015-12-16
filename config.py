# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
"""
flask automagically includes ALL_CAPS values in the app.config object
(see main.py app.config.from_object)
"""
DEBUG = True
TEMPLATE_DEBUG = False

# path to use when daemonized
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, ".env"))

APP_SECRET_KEY = os.environ["APP_SECRET_KEY"]
COUCHDB_SERVER = os.environ["COUCHDB_SERVER"]
COUCHDB_DATABASE = os.environ["COUCHDB_DATABASE"]

USERS = {
        "doug.shawhan@gmail.com": {
            "password": "g33k3r",
            "role": "admin"
            }
        }

del os
