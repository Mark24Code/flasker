from flask import Blueprint

bp = Blueprint('Sample',
               __name__,
               url_prefix='/sample',
               template_folder='templates'
               )

from sample import views,models
