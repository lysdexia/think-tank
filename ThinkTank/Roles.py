# -*- coding: utf-8 -*-
from flaskext.auth import Auth, AuthUser, Role, Permission

def auth_roles(app):
    auth = Auth(app, login_url_name="login")
    auth.user_timeout = 0

    # permission = Permission(resource, action)
    read_posts = Permission("read", "posts")
    create_subject = Permission("create", "subject")
    administer_things = Permission("administer", "things")

    roles = {
            "user": Role("user", [read_posts]),
            "annointed": Role("annointed", [read_posts, create_subject]),
            "admin": Role("admin",
                [read_posts, create_subject, administer_things])
            }
    
    def load_role(role_name):
        return roles.get(role_name)

    auth.load_role = load_role
    return auth

