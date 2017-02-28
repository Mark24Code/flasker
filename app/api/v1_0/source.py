"""
认证
"""
from flask_restful import Resource
from . import restful_api
from . import multi_auth


class Source(Resource):
    decorators = [multi_auth.login_required]

    def get(self):
        return {
            'status': 200,
            'msg': 'Get source restful'
        }

    def post(self):
        return {
            'status': 200,
            'msg': 'POST source restful'
        }

    def put(self):
        return {
            'status': 200,
            'msg': 'PUT source restful'
        }

    def delete(self):
        return {
            'status': 200,
            'msg': 'DELETE source restful'
        }

restful_api.add_resource(Source, '/source')
