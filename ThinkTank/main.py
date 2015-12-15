# -*- coding: utf-8 -*-
from flask import Flask, g
from flaskext.auth import Auth, AuthUser, Role, Permission
from ThinkTank.Routes import routes

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["APP_SECRET_KEY"]

auth = Auth(app, login_url_name="login")
auth.user_timeout = 0

# permission = Permission(resource, action)
read_posts = Permission("read", "posts")
create_subject = Permission("create", "subject")
administer_things = Permission("administer", "things")
roles = {
        "user": Role("user", [read_posts]),
        "annointed": Role("annointed", [read_posts, create_subject]),
        "admin": Role("admin", [read_posts, create_subject, administer_things])
        }

def load_role(role_name):
    return roles.get(role_name)
auth.load_role = load_role

# initialize routes
routes(app)

@app.before_request
def init_users():
    g.users = {}
    g.roles = {}
    for email in app.config["USERS"]:
        user = AuthUser(username=email)
        user.set_and_encrypt_password(app.config["USERS"][email]["password"])
        user.role = app.config["USERS"][email]["role"]
        g.users[email] = user
        g.roles[email] = app.config["USERS"][email]["role"]




