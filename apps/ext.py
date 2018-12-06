
# 初始化第三方插件
def ext_db():
    pass



# 初始化数据库操作
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
def init_db(app):
    #dialect+driver://username:password@host:port/database
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@127.0.0.1:3306/flask_orm2?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 打印sql语句
    app.config['SQLALCHEMY_ECHO']=True
    # 自动提交事物
    # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    db.init_app(app=app)
    migrate.init_app(app,db)