# -*- coding: utf-8 -*-
import datetime
import uuid
from flask import render_template, abort, request, session, redirect, url_for, g
from flaskext.auth import AuthUser, permission_required, logout
from flaskext.auth.models.sa import get_user_class

def routes(app, db): 
    User = get_user_class(db.Model)

    def user_create():
        if request.method == 'POST':
            username = request.form['username']
            if User.query.filter(User.username==username).first():
                return 'User already exists.'
            password = request.form['password']
            user = User(username=username, password=password, role="admin")
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        return '''
                <form method="POST">
                    Username: <input type="text" name="username"/><br/>
                    Password: <input type="password" name="password"/><br/>
                    <input type="submit" value="Create"/>
                </form>
            '''
    app.add_url_rule('/users/create/', 'user_create', user_create, methods=['GET', 'POST'])

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

            """
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

            """

            user = User.query.filter(User.username==email).one()
            if user is not None:
                if not user.authenticate(request.form["password"]):
                    return render_template(
                        "login.html",
                        error = "Incorrect password for %s."%email,
                        email = email)
                return redirect(url_for("index"))
        return render_template("login.html")

    @app.route("/logout")
    def logmeout():
        logout()
        return redirect(url_for("login"))
