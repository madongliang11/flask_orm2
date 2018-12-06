import datetime

from apps.ext import db


# 一级菜单
class Category(db.Model):
    # 主键
    cate_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), unique=True, index=True, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    status = db.Column(db.Boolean, default=True)
    # userlist=True表示一对多 默认为True
    # userlist=False表示一对一
    '''
    lazy   select 表示一次性将所有的数据全部加载进内存
           dynamic 延迟加载（懒加载），先加载主表的数据，当我们去使用主表相关的数据的时候才去执行查询
    当数据比较多的时候建议使用dynamic
    '''
    subs = db.relationship('SubCategory',lazy='dynamic',backref='category')

# 二级菜单
class SubCategory(db.Model):
    sub_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 创建外键字段
    # 主表类名.主键字段 或者 主表表名.列名（'category.cate_id'）
    # 如果给表名或者列名起别名，要换成别名
    cate_id = db.Column(db.Integer,db.ForeignKey(Category.cate_id))
    name = db.Column(db.String(60), unique=True, index=True, nullable=False)
    sort = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    status = db.Column(db.Boolean, default=True)
    is_delete = db.Column(db.Boolean, default=True)
    types = db.relationship('CategoryType', lazy='dynamic', backref='categoryType')

# 三级菜单
class CategoryType(db.Model):
    type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sub_id = db.Column(db.Integer, db.ForeignKey(SubCategory.sub_id,ondelete='CASCADE'))
    name = db.Column(db.String(60), unique=True, index=True, nullable=False)
    sort = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    status = db.Column(db.Boolean, default=True)
    is_delete = db.Column(db.Boolean, default=True)

