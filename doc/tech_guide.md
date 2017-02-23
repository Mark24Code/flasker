### 技术栈指南

---
### 1.开发工具
#### Sublime

* settings json

    ```json
    {
        "bold_folder_labels": true,
        "default_encoding": "UTF-8",
        "draw_white_space": "all",
        "file_exclude_patterns":
        [
        ],
        "folder_exclude_patterns":
        [
            "node_modules"
        ],
        "font_face": "Consolas",
        "font_size": 16,
        "ignored_packages":
        [
            "Vintage"
        ],
        "save_on_focus_lost": true,
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
        "trim_trailing_white_space_on_save": true
    }
    ```
* Plugins List:

    * 自动化注释：[Doc​Blockr_Python](https://packagecontrol.io/packages/DocBlockr_Python)

---

### 2.技术栈

* Python 3.5+
    * 注释：Python3.6加入异步/协程支持；Flask 0.12支持Python3.6

* Flask  0.11+
    * 注释：从0.11开始，是更好的适配Python3的版本。

*  [Flask-Restful 0.35+](http://flask-restful.readthedocs.io/en/0.3.5/)

    * 注释: [0.35增加了对蓝图的支持](http://flask-restful.readthedocs.io/en/0.3.5/intermediate-usage.html#use-with-blueprints)；只使用 1.类结构 2.请求解析，可以解决繁杂的后端校验。输出解析太冗余，不够灵活。

### 3.代码规范


* 代码风格:
    * [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
    * [Pocoo 风格指引](http://www.pythondoc.com/flask/styleguide.html)
* 注释风格:
    * [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
    * [Sphinx 风格](http://www.pythondoc.com/flask/styleguide.html)

Pocoo风格是为了和Flask的风格保持一致，可以不断地学习和参考。并且接近PEP8。

Sphinx的注释风格，和Flask保持一致，且可以导出注释生成文档。使用的格式化语言reStructuredText（Pycharm默认docstrings风格）

> 注释：Sphinx 是一种文档工具，它可以令人轻松的撰写出清晰且优美的文档, 由 Georg Brandl 在BSD 许可证下开发. 新版的Python文档 就是由Sphinx生成的， 并且它已成为Python项目首选的文档工具,同时它对 C/C++ 项目也有很好的支持; 并计划对其它开发语言添加特殊支持. 它采用reStructuredText(一种标记语言)!

### 4.架构设计

* 目录结构设计：[Flask最佳实践](https://zhuanlan.zhihu.com/p/22774028?refer=python-cn)

* application 的概念: 一个application一个蓝图。

  任何具体的东西，都是独立的松散的。只有一个抽象的东西，能够达到聚合作用。

  application应该通过页面集合和API集合提供一组独立的功能。具有顶层的抽象性。models里面，会存在数个表结构，来支撑一个蓝图app的状态。
  (如果通过页面划分，会相当冗余。)

  app将会是 资源API的参考。Restful的API尽量和App保持一致的平行目录。


### 5.约定

* HTTP 状态码：
    * 200 OK(成功)
    * 201 Created(创建成功)
    * 400 Bad Request(坏请求)
    * 401 Unauthorized(未授权)
    * 403 Forbidden(禁止)
    * 404 Not Found(未找到)
    * 405 Method Not Allowed(不允许使用的方法)
    * 500 Internal Server Error(内部服务器错误)

* Response 格式：
  app的划分也不是绝对的。是平衡的结果。因为作为一个网站，我们当然希望业务彼此松耦合，这样子可插拔。可是现实中，网站又是一个整体，彼此会有强弱联系。比如用户Auth系统，通知系统，都是关联非常多的蓝图。但是大原则是不变的，除了直觉上关联性强的，强耦合，不建议，人为制造强耦合。

    ```json
    {
        status:<HTTP 状态码>,
        message:<提示消息>,
        data:<返回数据>
    }
    ```