#! /usr/bin/env python
# -*- coding: utf-8 -*-

# '''
# 配置文件
# '''
import os
import re
# 项目的根目录
CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

DATA_HOST = '120.77.43.52'
DATA_USER = 'root'
DATA_PASSWORD = ''
DATA_DB = 'lovearrive'
DATA_CHARSET = 'utf8'

DATA_HOST_PD= '123.207.41.119'
DATA_USER_PD = 'root'
DATA_PASSWORD_PD = ''
DATA_DB_PD = 'lovearrive'
DATA_CHARSET_PD = 'utf8'

# 半塘如果限制了爬的速度 限制访问的频率
SLEEP = 0.5

# 万一请求断开了，多久以后再次访问呢
BANTANG_SLEEP  = 1200

# 感谢代理提供商
PROXY_SITES = [
    'http://www.xicidaili.com',
]

REFERER_LIST = [
    'http://www.google.com/',
    'http://www.bing.com/',
    'http://www.baidu.com/',
]

# 匹配ip地址的正则
PROXY_REGEX = re.compile('[0-9]+(?:\.[0-9]+){3}:\d{2,4}')

TIMEOUT = 5

# links.bin的项目路径
LINKS_BIN = os.path.join(CONFIG_DIR, "links.bin")


###########################################
#                   分词相关               #
###########################################
# 分词文件存储位置
SEARCH_PARTICIPLE_PATH = 'store'
SEARCH_PARTICIPLE_PATH = os.path.join(CONFIG_DIR, SEARCH_PARTICIPLE_PATH)

# 分词文件存储格式
SEARCH_PARTICIPLE_FILE_NAME = 'search.big'

# 一个文件夹放多少个分词文件夹
SEARCH_PARTICIPLE_SIZE = 500
