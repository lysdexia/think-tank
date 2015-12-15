import re
import time
import uuid
from flask import request, session, g
from flask.ext import restful
from flask_restful import reqparse
from flaskext.auth import AuthUser, permission_required, logout
def api(app):

    class Auth(restful.Resource):
        """
        """
        def post(self):
            doc = request.get_json()
            if not all([
                "email" in doc and doc["email"],
                "password" in doc and doc["password"],
                ]):
                restful.abort(401, message="email and password required")

            try:
                if not g.users[doc["email"]].authenticate(doc["password"]):
                    restful.abort(401, message="Incorrect login")
            except Exception as error:
                print(error)
                restful.abort(401, message="Incorrect login")

            token = str(uuid.uuid4())
            g.tokens[doc["email"]] = {
                    "token": token,
                    "stamp": time.time(),
                    }
            return {
                    "token": token,
                    "email": doc["email"],
                    }


    api = restful.Api(app)
    api.add_resource(Auth, "/api/auth")
