#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
这是所有爬虫的基类
'''

import re
import time
import json
import requests

from public.db.coupon_db import CouponDB

class BaseSpider(object):
    '''
    爬虫的基类思密达
    '''
    def __init__(self):
        self.re_id = re.compile(r'(.*)g/(\d{1,3})(.*)')
        self.coupon_db = CouponDB()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        }

    def get_time_now(self):
        """
        获取当前时间的毫秒数
        :return:
        """
        return time.time()

    def timestamp_to_date_str(self, timestamp):
        '''
        时间戳转化为字符串：2017-05-06 23:59:59
        :param timestamp:时间戳
        :return:
        '''
        if not timestamp:
            return None
        if not isinstance(timestamp, int):
            # 只有Int的类型才能转换
            timestamp = int(timestamp)
            return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

    def date_str_to_timestamp(self, datestr):
        """
        把2017-05-06 23:59:59类型的字符串转换成时间戳
        :param datestr: 2017-05-06 23:59:59 字符串
        :return: 时间戳
        """
        return time.mktime(time.strptime(datestr, '%Y-%m-%d %H:%M:%S')) if datestr else None

    def strip_space(self, character):
        """
        去除字符串的空格，制表符，换行符
        :param character: 将要去除的字符
        :return: 去除了空格，制表符，换行符的字符
        """

        return "".join(character.split())

    def get_id_for_url(self, url):
        """
        从url中获取id
        :param text: url
        :return:
        """
        result = re.search(self.re_id, url)
        if len(result.groups()) > 0:
            return result.group(2)
        else:
            return None