# -*- coding: utf-8 -*-
__author__ = 'Apple'

class Coupon(object):
    """
        商品信息的实体类
    """

    def __init__(self):
        # 主键id
        self.id = None
        # 二级分类的id
        self.second_id = None
        # 一级分类的id
        self.first_id = None
        # 商品的title
        self.title = None
        # 商品的价格
        self.price = None
        # 商品的url
        self.url = None
        # 商品的图片
        self.thumbnail_pic = None

    def __str__(self):
        return '(Coupon: %s,%s,%s, %s, %s, %s, %s, %s,%s)' % (self.title, self.price,
                                                     self.second_id,self.first_id, self.url,
                                                     self.thumbnail_pic)


class Page(object):
    '''
    分页对象
    '''

    def __init__(self):
        # 一页的数量
        self.page_size = None
        # 当前页
        self.page_index = None
        # 总页数
        self.page_count = None
        # 记录
        self.total = None

    def __str__(self):
        def __str__(self):
            return ('(page_index:%s, page_size:%s, total:%s, page_count:%s)'
                   % (self.page_index, self.page_size, self.total, self.page_count))

    __repr__ = __str__
