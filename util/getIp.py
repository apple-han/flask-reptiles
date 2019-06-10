# -*- coding: utf-8 -*-
from header_pool import user_agent

__author__ = '__apple'
__time__ = '2018/1/18 15:10'

import random

import requests
from public.settings import TIMEOUT


def fetch(url):
    # 获取随机的代理
    proxy = require_proxy()
    # 随机的header
    headers = {'User-Agent': random.choice(user_agent)}
    s = requests.Session()
    proxies = None
    if proxy is not None:
        proxies = {
            'http': proxy,
        }
    return s.get(url, timeout=TIMEOUT, proxies=proxies, headers=headers)

# 获取proxy require_proxy
def require_proxy():
    from proxypool.setting import PROXY_POOL_URL
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
