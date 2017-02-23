"""
认证
"""
from flask_restful import Resource
from . import restful_api
from . import auth


class Source(Resource):
    @auth.login_required
    def get(self):
        return {'msg': 'Get source restful'}

    @auth.login_required
    def post(self):
        return {'msg': 'POST source restful'}

    @auth.login_required
    def put(self):
        return {'msg': 'PUT source restful'}

    @auth.login_required
    def delete(self):
        return {'msg': 'DELETE source restful'}

restful_api.add_resource(Source, '/source')
