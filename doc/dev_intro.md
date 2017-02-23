### 开发指南

---

### 后台系统

step1:进入项目目录，写入系统变量

```shell
export FLASK_APP=<app实例所在目录>
export FLASK_CONFIG=<启动模式: develop/production/test>
```
注释： Windows下，export改为 set

step2:初始化数据库

```shell
flask init_db
```

step3:生成数据库版本仓库

```shell
flask db init
```


每次修改数据库后，执行

```shell
flask db migrate
flask db upgrade
```

注释：
[Flask-Migrate Doc](https://flask-migrate.readthedocs.io/en/latest/)
```shell
# 首次需要执行
flask db init # 生成migrations,数据库版本控制仓库

# 每次更新表结构后，按顺序执行
flask db migrate # 生成初始迁移(根据模型生成迁移脚本)
flask db upgrade # 把迁移用于数据库(运行迁移脚本，执行其SQL语句，作用于数据表)

# 数据库迁移顺序: models -> scripts -> tables

flask db --help # 获取帮助列表
```