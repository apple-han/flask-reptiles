# -*- coding: utf-8 -*-
__author__ = 'Apple'

import os

from base.log import start_log
from spider import bantang

# 启动日志
start_log(file_path="spider" + os.sep + "bt")
# 启动半糖爬虫
bantang.start()
