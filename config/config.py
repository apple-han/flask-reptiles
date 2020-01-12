#! /usr/bin/env python
# -*- coding: utf-8 -*-

# '''
# 配置文件
# '''
import os,re
# 项目的根目录
CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

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

EXPIRE = 15 * 24 * 3600

# 匹配ip地址的正则
PROXY_REGEX = re.compile('[0-9]+(?:\.[0-9]+){3}:\d{2,4}')

TIMEOUT = 5
# 一页多少条数据
PER_PAGE = 10

DEBUG = True

# links.bin的项目路径
LINKS_BIN = os.path.join(CONFIG_DIR, "links.text")

UPLOAD_PATH = os.path.join(CONFIG_DIR, "image")


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



# 数据库相关, 设置密码, 手动创建数据库
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.31.231/products'

SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'

# 兼容window
SQLALCHEMY_TRACK_MODIFICATIONS = False