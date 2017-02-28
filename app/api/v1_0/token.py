"""
生成电子令牌
"""
from flask import g
from flask_restful import Resource
from . import restful_api
from . import basic_auth


class Token(Resource):
    decorators = [basic_auth.login_required]

    def get(self):
        token = g.current_user.generate_auth_token()
        return {
            'status': 200,
            'message': 'token',
            'data': {
                'token': token.decode('ascii')
            }
        }


restful_api.add_resource(Token, '/token')
