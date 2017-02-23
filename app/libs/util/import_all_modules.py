"""
导入指定包下的所有模块
"""
from werkzeug.utils import find_modules, import_string


def import_all_modules(root_name, include_packages=False, recursive=False):
    """
    导入指定根目录下所有包和模块
    root_name 模块名字符串，以点号分隔(或者 非 top_level 时的__name__属性);
    :param root_name: the dotted name for the package to find child
    :param include_packages: set to True if packages should be returned, too.
    :param recursive: set to True if recursion should happen.
    :return: generator
    """
    mods = find_modules(root_name, include_packages, recursive)
    for mod in mods:
        import_string(mod)
