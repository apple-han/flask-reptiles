# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/17 16:24'

import re

from public.db.data_base import DataBase
from public.model import Page
from public.encoder.commodity_encoder import CommodityEncoder

'''
    所有异常的父类
'''
class BaseHandler(Exception):

    def __init__(self):
        super(BaseHandler, self).__init__()
        self.db = DataBase()
        self.success = {"status":"success","message":"成功"}
        self.error_message = {"status": "error"}
        self.not_found = {"status": "not found", "message": "查询商品不存在"}
        self.number = re.compile(r'0|([1-9]\d*)')
        self.float_number = re.compile(r'\d+\.\d+')
        # 防止sql注入
        self.sql_into = re.compile(r'([a-zA-Z0-9\(\)\=])*')
        self.page = Page()

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET')

    def __reverse_number__(self, count,float_num=False):
        '''
        判断是否是数字
        :param count:需要匹配的字符串
        :param float_num:
        :return:
        '''
        if count is None:
            return False
        number_str = str(count)

        if float_num:
            result = re.match(self.float_number, number_str)
            if result:
                return float(result.group())
            else:
                return False
        else:
            result = re.match(self.number, number_str)
            if result:
                return int(result.group())
            else:
                return False

    def verification_page_volume(self, page, volume):
        '''
        验证分页和排序是否符合当前的规则
        :param page:
        :param volume:
        :return:
        '''

        page_index = page.page_index
        page_size = page.page_size

        if page_index <= 0 or page_size > 100:
            return False

        if volume not in (0,1,2,3):
            return False
        return True