"""
定制化处理
"""
from flask import render_template, request, jsonify


def is_api_req(req):
    if '/api' in req.path:
        return True
    else:
        return False


def set_error_handlers(app):
    @app.errorhandler(404)
    def page_not_found(error):
        if is_api_req(request):
            return jsonify({
                'status': 400,
                'message': 'sources not found',
                'data': {}
            }), 404
        return render_template('404.html'), 404

    @app.errorhandler(403)
    def forbidden(error):
        if is_api_req(request):
            return jsonify({
                'status': 403,
                'message': 'not forbidden',
                'data': {}
            }), 403
        return render_template('403.html'), 403

    @app.errorhandler(500)
    def server_error(error):
        if is_api_req(request):
            return jsonify({
                'status': 500,
                'message': 'server error',
                'data': {}
            }), 500
        return render_template('500.html'), 500
