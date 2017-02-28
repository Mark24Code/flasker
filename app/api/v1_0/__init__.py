"""
API v1.0
"""
from flask import Blueprint, g, jsonify
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth
from flask_restful import Api, Resource

from app.libs.util import import_all_modules
from app.auth.models import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth('JWT')
multi_auth = MultiAuth(basic_auth, token_auth)


@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.current_user = user
    return True


@token_auth.verify_token
def verify_token(token):
    if token:
        user = User.verify_token(token)
        if user:
            g.current_user = user
            return True
        else:
            return False
    else:
        return False


@basic_auth.error_handler
def unauthorized(message=None):
    return jsonify({
        'status': 403,
        'message': message or 'forbidden',
        'data': {}
    }), 403


bp = Blueprint('api.v1_0',
               __name__,
               url_prefix='/api/v1.0')

restful_api = Api(bp)

import_all_modules(__name__)

from . import errors
