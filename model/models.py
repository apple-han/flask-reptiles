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