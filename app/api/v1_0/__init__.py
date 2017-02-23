"""
API v1.0
"""
from flask import Blueprint, g, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource

from app.libs.util import import_all_modules
from app.auth.models import User

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.current_user = user
    return True


@auth.error_handler
def unauthorized(message=None):
    return jsonify({
        'status': 403,
        'message': message or 'forbidden',
        'data': {}
    }), 403


bp = Blueprint('api',
               __name__,
               url_prefix='/api/v1.0')

restful_api = Api(bp)

import_all_modules(__name__)

from . import errors
