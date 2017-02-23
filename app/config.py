import os

BASEDIR = os.path.abspath(os.path.dirname(__name__))

# app文件名
APP_MODULE_NAME = 'app'

# 拓展列表
EXTENSIONS_LIST = [
    'db'
]

# Web Auth, LoginManager Session
SESSION_PROTECTION = 'strong'
LOGIN_VIEW = 'auth.login'


class Config(object):
    """基础配置"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(Config):
    """开发配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATEBASE_URL') or \
                              'sqlite:///' + os.path.join(BASEDIR, 'devDB.sqlite')


class TestConfig(Config):
    """测试配置"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATEBASE_URL') or \
                              'sqlite:///' + os.path.join(BASEDIR, 'testDB.sqlite')


class PrdConfig(Config):
    """生产配置"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATEBASE_URL') or \
                              'sqlite:///' + os.path.join(BASEDIR, 'prdDB.sqlite')


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': PrdConfig,
    'default': DevConfig
}
