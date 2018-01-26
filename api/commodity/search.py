import json

from flask.ext.restful import Resource
from flask import request
from collections import Counter

from public.encoder.commodity_encoder import CommodityEncoder
from public.db.search_db import SearchDB
from util.search import chinese_to_number, splicing_path
from util import os_path
from public.model import Page
from api.handlers.BaseHandler import BaseHandler
import jieba


class SearchAPI(Resource,BaseHandler):
    def __init__(self):
        super(SearchAPI, self).__init__()
        self.search_db = SearchDB()

    def data_received(self, chunk):
        pass

    def get(self):
        key = request.args.get("key")
        # 替换所有的空格
        key = key.replace(' ', '')
        self.page.page_index = self.__reverse_number__(request.args.get("page_index", 1))
        self.page.page_size = self.__reverse_number__(request.args.get('page_size', 50))
        volume = self.__reverse_number__(request.args.get("volume", 0))

        self.page.page_count = 0
        self.page.total = 0

        if self.verification_page_volume(self.page, volume):
            start_index = (self.page.page_index-1) * self.page.page_size
            end_index = start_index + self.page.page_size
            if key:
                result = self.split_name(key)
                if result:
                    ids = list()
                    for r in result:
                        codes = chinese_to_number(r)
                        if codes[0]:
                            files = splicing_path(codes[1])
                            file_list = os_path.read_file_to_search(files.get('file_path'))
                            if file_list:
                                ids += file_list
                    if ids:
                        store_ids = Counter(ids)
                        # 获取记录总数
                        self.page.total = len(store_ids)
                        # 得到总页数
                        self.page.page_count = int(self.page.total / self.page.page_size)
                        # 最后一页可能除不尽
                        if self.page.page_count > 0:
                            if self.page.page_count > int(self.page.page_count):
                                # 说明除不尽，还有一页
                                self.page.page_count = int(self.page.page_count) + 1
                            else:
                                self.page.page_count = int(self.page.page_count)
                        total_ids = store_ids.most_common(self.page.total)
                        select_ids = total_ids[start_index:end_index]
                        sid = ''
                        for si in select_ids:
                            sid = sid + si[0] + ','
                        if sid:
                            sid = sid[:-1]
                            self.success['data'] = self.search_db.find_commoditys_by_ids(sid, volume)
                            page = {
                                'page_size':self.page.page_size,
                                'page_index':self.page.page_index,
                                'page_count':self.page.page_count,
                                'total': self.page.total
                            }
                            self.success['page'] = page
                            return json.dumps(self.success, cls=CommodityEncoder)
                        else:
                            return self.not_found
                    else:
                        return self.not_found
                else:
                    return self.error_message
            else:
                return self.error_message
        else:
            return self.error_message


    def split_name(self,name):
        '''
        把搜索的条件进行拆分
        :param name:
        :return:
        '''
        name = jieba.lcut_for_search(name)
        return name