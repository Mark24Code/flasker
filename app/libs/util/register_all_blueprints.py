
from werkzeug.utils import find_modules, import_string
from app.config import APP_MODULE_NAME


def register_all_blueprints(app):
    """
    批量注册蓝图

    导入app目录下所有蓝图
    :param app: Flask实例
    :return: None
    """
    for mod in [mod for mod in find_modules(APP_MODULE_NAME, include_packages=True, recursive=True)]:
        mod = import_string(mod)
        nsp = dir(mod)
        if 'bp' in nsp:
            app.register_blueprint(mod.bp)
