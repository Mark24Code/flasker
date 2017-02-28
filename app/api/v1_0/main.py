"""
首页资源
"""
from flask_restful import Resource
from . import restful_api
from . import multi_auth


class Index(Resource):
    decorators = [multi_auth.login_required]

    def get(self):
        return {
            'status': 200,
            'msg': 'Get 来自蓝图restful'
        }

    def post(self):
        return {
            'status': 200,
            'msg': 'POST 来自蓝图restful'
        }

    def put(self):
        return {
            'status': 200,
            'msg': 'PUT 来自蓝图restful'
        }

    def delete(self):
        return {'msg': 'DELETE 来自蓝图restful'}


restful_api.add_resource(Index, '/index')
