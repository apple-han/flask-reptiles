# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/18 16:00'

from gevent.pool import Pool
from requests.exceptions import RequestException

from util.getIp import fetch
from public.db.coupon_db import CouponDB

pool = Pool(10)

def check_proxy(p):
    try:
        fetch('http://baidu.com', proxy=p['ip'])
    except RequestException as e:
        CouponDB().delete_ip(p['id'])

#print(CouponDB().sumip())
pool.map(check_proxy, CouponDB().sumip())

