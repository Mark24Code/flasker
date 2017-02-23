"""
首页资源
"""
from flask_restful import Resource
from . import restful_api
from . import auth


class Sample(Resource):
    @auth.login_required
    def get(self):
        return {'msg': 'Get 来自Sample蓝图restful'}

    @auth.login_required
    def post(self):
        return {'msg': 'POST 来自Sample蓝图restful'}

    @auth.login_required
    def put(self):
        return {'msg': 'PUT 来自Sample蓝图restful'}

    @auth.login_required
    def delete(self):
        return {'msg': 'DELETE 来自Sample蓝图restful'}


restful_api.add_resource(Sample, '/sample')
