#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '__apple'

from public.db.participle_db import DataBase_PD


class SearchDB(DataBase_PD):
    def __init__(self):
        super().__init__()

    def find_commoditys(self, this_page=None, page_size=None, effective_status=True):
        """
            从数据库获取商品信息
        :param size: 一次获取多少个
        :param status: 1 获取有效期内的商品 0 获取过期商品
        :return:
        """
        sql = """
            select id, title, goods_desc from goods_goods {data_sql} 
        """
        effective = "limit {this_page}, {page_size}"

        sql = sql.format(data_sql= effective)
        sql = sql.format(this_page=this_page, page_size=page_size)
        self.log.info('[INFO] GET goods_goods: this_page:{0} - page_size:{1}'.format(this_page, page_size))

        return self.find_execute(sql, fetchone=False)

    def find_commoditys_by_ids(self, sid, volume=0):
        """
        通过id来查询商品信息，并且按照查询顺序展示
        :param sid:
        :return:
        """
        # 排序规则
        volume_sql = {
            "volume_sql_0": " ORDER BY INSTR(',{sid},',CONCAT(',',id,',')) ",
            "volume_sql_1": "order by click_num desc",
            "volume_sql_2": " order by price asc ",
        }

        sql = """
            select * from goods_goods where id in ({sid})
        """

        order_sql = 'volume_sql_' + str(volume)
        sql = sql + volume_sql.get(order_sql)
        return self.find_execute(sql.format(sid=sid), (), fetchone=False)