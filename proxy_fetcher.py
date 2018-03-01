# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/18 15:16'


import threading
from multiprocessing.dummy import Pool as ThreadPool
import re

import requests

from public.db.data_base import DataBase
from util.getIp import fetch
from public.settings import PROXY_REGEX, PROXY_SITES
from public.db.coupon_db import CouponDB
from public.base_spider import BaseSpider


class SaveIp(DataBase,BaseSpider):

    def operation(self,url):
        try:
            r = fetch(url)
        except requests.exceptions.RequestException:
            return False
        addresses = re.findall(PROXY_REGEX, r.text())
        for address in addresses:
            time = self.timestamp_to_date_str(self.get_time_now())
            try:
                CouponDB().save_ip(address, time)
            except Exception:
                pass

def use_thread_pool():
    pool = ThreadPool(5)
    pool.map(SaveIp().operation, PROXY_SITES)
    pool.close()
    pool.join()

if __name__ == '__main__':
    use_thread_pool()