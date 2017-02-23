# !/usr/bin/env python3
"""
app.__init__

app入口文件（相当于main.py）
"""
from flask import Flask

from .exts import db, login_manager, bootstrap, moment
from .config import config, APP_MODULE_NAME, SESSION_PROTECTION, LOGIN_VIEW
from .errors import set_error_handlers
from app.libs.util import register_all_blueprints


def create_app(config_name):
    """
    Flask实例工厂函数

    导入配置
    初始化拓展
    注册蓝图
    :param config_name:字符串类型，配置模式（default,development,testing,production）
    :return: 设置完毕的Flask实例
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # errors handlers
    set_error_handlers(app)

    # register all blueprints
    register_all_blueprints(app)

    # install extensions
    # bootstrap
    bootstrap.init_app(app)
    # time
    moment.init_app(app)
    # database
    db.init_app(app)

    # login manager (web auth)
    login_manager.session_protection = SESSION_PROTECTION
    login_manager.login_view = LOGIN_VIEW
    login_manager.init_app(app)

    return app
