# -*- coding: utf-8 -*-
__author__ = 'Apple'

import os

from public.log import start_log
from spider.main import start_bt

# 启动日志
start_log(file_path="spider" +os.sep+ "bt")
# 启动半糖爬虫
start_bt()