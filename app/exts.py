"""app.exts

统一管理Flask扩展，方便解耦。
参考：[Flask最佳实践](https://zhuanlan.zhihu.com/p/22774028?refer=python-cn)
"""
from app.config import SESSION_PROTECTION, LOGIN_VIEW

# default
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_httpauth import HTTPBasicAuth
from flask_bootstrap import Bootstrap
from flask_moment import Moment

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
moment = Moment()
http_auth = HTTPBasicAuth()


# development
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension()

# testing

# production
