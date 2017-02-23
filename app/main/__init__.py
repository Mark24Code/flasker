from flask import Blueprint
from app.exts import http_auth


bp = Blueprint('main',
               __name__,
               url_prefix='',
               template_folder='templates',
               static_folder='static')

from . import views, errors
