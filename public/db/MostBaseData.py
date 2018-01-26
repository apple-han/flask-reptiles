#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
操作数据库
'''

from public import log
import pymysql.cursors
# from public.settings import (DATA_HOST,DATA_USER,DATA_PASSWORD,
#                              DATA_DB,DATA_CHARSET)

class MostBase(object):
    def __init__(self):
        self.connection = pymysql.connect(
                                    host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    db=self.db,
                                    charset=self.data_charset,
                                    cursorclass=pymysql.cursors.DictCursor)
        self.log = log.logging

    def execute(self, sql, execute_data=None):
        '''
        执行sql
        :param sql:
        :param execute_data:
        :return:
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, execute_data)
            self.connection.commit()
        except Exception as e:
            print(e)
            self.log.info(e)
            self.connection.rollback()
    def close(self):
        self.connection.close()

    def find_execute(self, sql,execute_data=None,fetchone=True,many_size=None):
        '''
        查询sql
        :param sql:执行的SQL
        :param execute_data:查询的数据
        :param fetchone:是否只查询一条
        :param many_size:查询的大小
        :return:
        '''
        with self.connection.cursor() as cursor:
            cursor.execute(sql, execute_data)
            if many_size:
                result = cursor.fetchmany(many_size)
            elif fetchone:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
            return result
