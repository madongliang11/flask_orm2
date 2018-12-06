from flask import Flask
from apps.ext import init_db

# 入口函数
from apps.orm.views import orm


def create_app():
    app = Flask(__name__)
    app.debug = True
    # 注册蓝图
    register(app)
    # 初始化数据库相关配置
    init_db(app)
    return app

# 注册蓝图对象
def register(app:Flask):
    # 注册用户模块
    app.register_blueprint(orm,url_prefix='/orm/')
    pass