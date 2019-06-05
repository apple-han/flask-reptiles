# @Time    : 2019-06-03 20:11
# @Author  : __apple
from enum import IntEnum

from flask import current_app
from sqlalchemy import Column, Integer, String, orm, func
from model.base import Base, Pagination, db


class Volume(IntEnum):
    IDS = 0 # ids 排序
    PRICE = 1 # 价格

class Goods(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_id = Column(Integer, nullable=False)
    second_id = Column(Integer, nullable=False)
    title = Column(String(50))
    price = Column(Integer)
    url = Column(String(100))
    thumbnail_pic = Column(String(256))


    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'first_id', 'second_id',
                       'title',
                       'price','url', 'thumbnail_pic']


    @staticmethod
    def find_commoditys_by_ids(sid, page_no, collation=Volume.IDS):
        """
        通过id来查询商品信息，并且按照查询顺序展示
        :param sid:
        :return:
        """
        # 排序规则
        def re_volume(x):
            return {
                Volume.IDS:  func.INSTR(','+",".join(sid)+',',func.CONCAT(',',Goods.id,',')),
                Volume.PRICE: Goods.price,
            }.get(x, 0)

        from apple import app
        with app.app_context():
            query = Goods.query.filter(Goods.id.in_(sid))
            query = query.order_by(re_volume(collation))
            page_obj = Pagination(query, page_no, current_app.config['PER_PAGE'])
        return page_obj

    @staticmethod
    def find_commoditys(this_page=None, page_size=None):
        """
            从数据库获取商品信息
        :param size: 一次获取多少个
        :param status: 1 获取有效期内的商品 0 获取过期商品
        :return:
        """
        from apple import app
        with app.app_context():
            items = db.session.query(Goods.id, Goods.title).limit(page_size).offset(this_page).all()
        return items

    @staticmethod
    def save_coupon(coupon):
        '''
        保存一条商品信息到数据库
        :param coupon:
        :return:
        '''
        from apple import app
        with app.app_context():
            item = Goods.query.filter(Goods.title == coupon.title).first()
            if item : return False
            with db.auto_commit():
                goods = Goods()
                goods.first_id = coupon.first_id
                goods.second_id = coupon.second_id
                goods.title = coupon.title
                goods.price = coupon.price
                goods.url = coupon.url
                goods.thumbnail_pic = coupon.thumbnail_pic
                db.session.add(goods)
        return True
