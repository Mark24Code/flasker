from flask import Blueprint

bp = Blueprint('blog',
               __name__,
               url_prefix='/blog',
               template_folder='templates'
               )

from blog import views,models
