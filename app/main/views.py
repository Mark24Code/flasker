from flask import render_template
from . import bp


@bp.route('/index')
@bp.route('/home')
@bp.route('/')
def index():
    return render_template('main/index.html')
