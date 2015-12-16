# -*- coding: utf-8 -*-
import datetime
import uuid
from flask import render_template, abort, request, session, redirect, url_for, g
from flaskext.auth import AuthUser, permission_required, logout

def routes(app, couchdb, views): 

    def insert_user(email, password, role): 
        # you'll need to do an upsert first, then 
        # suck it all back out of the database and configure roles
        db_user = views.User(
                email = email,
                password = app.config["USERS"][email]["password"],
                role = app.config["USERS"][email]["role"],
                stamp = datetime.datetime.utcnow(),
                last_login = datetime.datetime.utcnow(),
                member_since = datetime.datetime.utcnow(),
                )
        db_user.save()

    def get_user(email):
        results = views.User.view("user/email", key=email).first()
        if results:
            doc = results._doc
            print(doc)

    def upsert_user(email, password, role):
        pass
       
    # grab static users from json
    # other users from db
    @app.before_request
    def init_users():
        g.tokens = {}
        g.users = {}
        g.roles = {}
        for email in app.config["USERS"]:
            user = AuthUser(username=email)
            user.set_and_encrypt_password(
                    app.config["USERS"][email]["password"])
            user.role = app.config["USERS"][email]["role"]

            g.users[email] = user
            g.roles[email] = app.config["USERS"][email]["role"]

    @permission_required(resource="read", action="posts")
    def index():
        return render_template("view.html", subject="everything")
    app.add_url_rule("/", "index", index)

    @permission_required(resource="read", action="posts")
    def browse():
        return render_template("browse.html")
    app.add_url_rule("/browse", "browse", browse)

    @permission_required(resource="read", action="posts")
    def view(subject):
        return render_template("view.html", subject=subject)
    app.add_url_rule("/s/<string:subject>", "view", view)
 
    @permission_required(resource="administer", action="things")
    def admin_block():
        return render_template("administration.html")
    app.add_url_rule("/admin", "admin_block", admin_block)

    # only register, login and logout don't require permissions

    @app.route("/register", methods = ["GET", "POST"])
    def register():
        if request.method == "POST":
            return redirect(url_for("index"))
        return render_template("register.html")

    @app.route("/login", methods = ["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form["email"]

            if "register" in request.form and request.form["register"]:
                return render_template(
                        "login.html",
                        error = "Registration token sent to %s."%email)

            if not email in g.users:
                return render_template(
                        "login.html", error = "%s not found."%email)

            if "forgot" in request.form and request.form["forgot"]:
                return render_template(
                        "login.html",
                        error = "Password reset sent to %s."%email)

            if not g.users[email].authenticate(request.form["password"]):
                return render_template(
                        "login.html",
                        error = "Incorrect password for %s."%email,
                        email = email)
            # make available for use by api calls
            session["email"] = email
            # friendly access_token for api to use
            session["access_token"] = str(uuid.uuid4())
            return redirect(url_for("index"))
        return render_template("login.html")

    @app.route("/logout")
    def logmeout():
        logout()
        return redirect(url_for("login"))
