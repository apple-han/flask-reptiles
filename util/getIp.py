# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/18 15:10'

import random

import requests
from fake_useragent import UserAgent

from public.settings import REFERER_LIST, TIMEOUT

def get_referer():
    return random.choice(REFERER_LIST)

def get_user_agent():
    ua = UserAgent()
    return ua.random

def fetch(url, proxy=None):
    s = requests.Session()
    proxies = None
    if proxy is not None:
        proxies = {
            'http': proxy,
        }
    return s.get(url, timeout=TIMEOUT, proxies=proxies)
