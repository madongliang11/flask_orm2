from flask import Blueprint, render_template
from sqlalchemy import and_, or_

from apps.orm.models import Category

orm = Blueprint('orm',__name__)


'''
select * from  表名
select 列名 别名,......from 表名
select 列名 别名，....from 表名 where 条件

select 列名 别名，...from 表名  
where 条件 
grou by 字段， having 分组过滤的条件
order_by 字段[DESC|ASC]....

多表
外连接  全连接（mysql不支持） 左连接
表名 别名 left out join 表名 别名
表名 别名 right out join 表名 别名
using(外键关联字段)  on 关联字段=关联字段
'''
@orm.route('/find/')
def find():
    # 可以使用关系运算符  !=  >  <  >=  <=  ==
    Category.query.filter(Category.name != '')
    # in like between and  and or
    # 等同于select * from Category where cate_id in (1,2,3)
    # query = Category.query.filter(Category.cate_id.in_([1,2,3]))
    # cate_list = query.all()

    # 模糊查询
    # select * from category where name like '%武%'
    cate_list=Category.query.filter(Category.name.like('%武%')).all()

    # and查询
    cate_list = Category.query.filter(Category.name.like('%武%'),Category.cate_id==1).all()
    cate_list = Category.query.filter(and_(Category.name.like('%武%'), Category.cate_id == 1)).all()

    #  or查询
    cate_list = Category.query.filter(or_(Category.name.like('%武%'), Category.cate_id == 2)).all()

    # between查询
    cate_list = Category.query.filter(Category.cate_id.between(1,10)).all()

    # 过滤列
    # 返回元组类似django中的value_list
    cate_list=Category.query.with_entities(Category.cate_id,Category.name).all()
    data = []
    for cate in cate_list:
        data.append({'cate_id':cate[0],'name':cate[1]})

    Category.query.filter_by()
    return render_template('cate.html',cate_list=data)

@orm.route('/list/<int:page>/<int:size>/')
def pagination_view(page,size):
    pagitation = Category.query.paginate(page=page,per_page=size,error_out=False)
    # 获取多少页
    print(pagitation.pages)
    # 当前分页的数据
    print(pagitation.items)
    # 总条数
    print(pagitation.total)
    # 当前的页码
    print(pagitation.page)
    # 是否有上一页
    print(pagitation.has_prev)
    # 是否有下一页
    print(pagitation.has_next)
    # 上一页显示多少条数据
    print(pagitation.prev_num)
    # 下一页显示多少条数据
    print(pagitation.next_num)
    '''
    left_edge=2 左边最少显示两条数据
    left_current=2 当前左边显示两条数据（不包含自己）
    right_current=5 当前右边显示5条记录（包含自己）
    right_edge=2 右边最少显示两条数据
    '''
    pagitation.iter_pages(left_edge=2,left_current=2,
                          right_current=5,right_edge=2)

    left_current =5
    right_current = 5
    if page < 6:
        right_current = 11 - page
    elif pagitation.pages - page < 5:
        left_current = 9 - (pagitation.pages - page)
    return render_template('pagination.html',pagitation=pagitation,right_current=right_current,left_current=left_current)


@orm.route('/cate/')
def cate():
    cates = Category.query.all()
    return render_template('cate.html',cates=cates)