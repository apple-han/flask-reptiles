#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
操作数据库
'''

from public import log
import pymysql.cursors
from .MostBaseData import MostBase
from public.settings import (DATA_HOST,DATA_USER,DATA_PASSWORD,
                             DATA_DB,DATA_CHARSET)

class DataBase(MostBase):
    def __init__(self):
        self.host = DATA_HOST
        self.user = DATA_USER
        self.password = DATA_PASSWORD
        self.db = DATA_DB
        self.data_charset = DATA_CHARSET

        super(DataBase, self).__init__()
