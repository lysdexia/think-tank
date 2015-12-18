# -*- coding: utf-8 -*-
import os
from dateutil.tz import tzlocal
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

# get local timezone
TIMEZONE = tzlocal()

APP_SECRET_KEY = os.environ["APP_SECRET_KEY"]

MONGOALCHEMY_CONNECTION_STRING = os.environ["MONGOLAB_URI"]
# bug in flask-mongoalchemy!
MONGOALCHEMY_DATABASE=os.environ["MONGOALCHEMY_DATABASE"]

del os
