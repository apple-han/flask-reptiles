# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/25 11:58'

'''
    分词读数据库用从库
'''

from public import log
import pymysql.cursors
from .MostBaseData import MostBase
from public.settings import (DATA_HOST_PD,DATA_USER_PD,DATA_PASSWORD_PD,
                             DATA_DB_PD,DATA_CHARSET_PD)

class DataBase_PD(MostBase):
    def __init__(self):
        self.host = DATA_HOST_PD
        self.user = DATA_USER_PD
        self.password = DATA_PASSWORD_PD
        self.db = DATA_DB_PD
        self.data_charset = DATA_CHARSET_PD

        super(DataBase_PD, self).__init__()