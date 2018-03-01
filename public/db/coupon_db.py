# -*- coding: utf-8 -*-
__author__ = 'Apple'

from public.db.participle_db import DataBase_PD


class CouponDB(DataBase_PD):
    def __init__(self):
        super(CouponDB, self).__init__()

    def save_coupon(self, coupon):
        '''
        保存一条商品信息到数据库
        :param coupon:
        :return:
        '''

        insert_sql = """
                    (insert into goods_goods(category_id,second_id,first_id,title, price, url, pic, brand,goods_desc,add_time)
                    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s))
                """
        old_coupon = self.is_has_by_name(coupon.title)
        insert_data = (
            coupon.category_id,coupon.second_id,coupon.first_id, coupon.title, coupon.price, coupon.url, coupon.pic
            , coupon.brand,coupon.goods_desc,coupon.add_time
        )

        if not old_coupon:
            return self.execute(insert_sql, insert_data)
        else:
            return False

    def is_has_by_name(self,title):
        '''
        根据name查询是否有这个商品
        :param title:
        :return:
        '''
        sql = """
                    select 1 from goods_goods where title = %s
                """
        return self.find_execute(sql, (title))


    def save_ip(self,ip,time):
        insert_sql = """
                    insert into goods_getip(ip,add_time) values (%s,%s)
                """
        return self.execute(insert_sql, (ip,time))

    def count_ip(self):
        select_sql = """
                    select count(*) from goods_getip
                """
        return self.find_execute(select_sql)

    def delete_ip(self,getip):

        delete_sql = """
                    DELETE FROM goods_getip WHERE id = {0}
                """
        print(delete_sql.format(getip))
        return self.execute(delete_sql.format(getip))

    def sumip(self):
        select_sql = """
                    select * from goods_getip
                """
        return self.find_execute(select_sql,fetchone=False)