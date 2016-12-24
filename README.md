# Flask 脚手架

##### Mark24Code
##### mark.zhangyoung@gmail.com

###目录结构：
                项目文件Project包含:
                1. app:中枢App
                    |-- static/ 静态文件目录
                    |-- templates/ 模板文件目录
                        |-- app:【tips:一定要和模块名想同】
                            |-- base.html 基础模板
                            |-- index.html 主页模板
                    |-- __init__.py 初始化文件【在此处，引用models,views】
                    |-- models.py 数据模型
                    |-- views.py 视图函数
                    |-- tests.py 自动化用例
                2. blog:蓝图App
                3. sample/:蓝图App模板例子
                    |--static/ 静态文件目录
                    |--templates/ 模板文件目录
                        |-- sample:【tips:一定要和模块名想同】
                            |-- base.html 基础模板
                            |-- index.html 主页模板

                    |-- __init__.py 初始化文件【在此处，引用models,views】
                    |-- models.py 数据模型
                    |-- views.py 视图函数
                    |-- tests.py 自动化用例
                4. env:存放Virtualenv虚拟环境
                5. migrations:迁移数据库自动生成目录
                6. db.sqlite:开发数据库
                7. initDB.py: 初始化数据库脚本
                8. manager.py: 存放自动化脚本
                9. README.md :说明文件
                10. requirement.txt :依赖列表
                11. run.py:入口文件 python run.py -h 0.0.0.0 -p 5000
                12. settings.py :配置信息

Tips:

1. views和 html中，引用模板使用 `app/index.html` 的格式
2. 插件式App使用蓝图声明，并在app 的 `__init__.py`中注册
   需要注意：
   1. 插件本身的`__init__.py` 声明蓝图
   2. 指定 `template_folder='templates'`
   3. 最后 `from sample import views,models`

3. 开启服务命令 `python run.py -h 0.0.0.0 -p 5000`
    访问 `http://127.0.0.1:5000`

4. 修改Models需要迁移数据库:

    1. `python run.py db init #第一次使用`
    2. `python run.py db migrate #生成修改比对`
    3. `python run.py db upgrade #更新数据库`

5. 初始化数据库 `python initDB.py`