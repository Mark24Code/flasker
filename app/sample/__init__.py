from flask import Blueprint

bp = Blueprint('sample',
               __name__,
               url_prefix='/sample',
               template_folder='templates',
               static_folder='static')

from . import views, errors
