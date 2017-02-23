"""
首页资源
"""
from flask_restful import Resource
from . import restful_api


class Index(Resource):
    def get(self):
        return {'msg': 'Get 来自蓝图restful'}

    def post(self):
        return {'msg': 'POST 来自蓝图restful'}

    def put(self):
        return {'msg': 'PUT 来自蓝图restful'}

    def delete(self):
        return {'msg': 'DELETE 来自蓝图restful'}


restful_api.add_resource(Index, '/index')
