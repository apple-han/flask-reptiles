#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
再次感谢半塘提供数据支持
'''
import urllib
import random
import json
from enum import IntEnum

from lxml import etree

from requests.exceptions import RequestException

from public.base_spider import BaseSpider
from public import log
from public.model import Coupon
from model.goods import Goods
from public.settings import LINKS_BIN
from util.getIp import fetch
from util.os_path import write_links, get_file_size, read_file_to_url, delete_line


class CouponList(IntEnum):
    ZERO = 0

class BanTang(BaseSpider):
    def __init__(self):
        super(BanTang,self).__init__()
        self.site_url = 'https://www.sqkb.com/g/14/'
        log.logging.info('[INFO] ============================================')
        log.logging.info('[INFO] Start site: {0}'.format(self.site_url))
        self.get_url = 'https://www.sqkb.com/g/getCouponTopicList/?cid={id}&sort=7&couponPage={page}&pagesize=40'

    def init_category(self):
        '''
        获取所有的一级分类
        :return:
        '''
        log.logging.info('[INFO] Get category')
        url = self.site_url

        try:
            res = fetch(url).text
        except RequestException as e:
            res = fetch(url).text
            log.logging.info('[warn] ineffective:{0}'.format(e))
        html = etree.HTML(res)
        # 一级分类
        root_brother = html.xpath("/html/body/div[3]/div/div/a")
        # 所有的一级分类请求url
        for rb in root_brother[::-1]:
            log.logging.info('[INFO] Get url: {0} >>> {1}'.format(rb.attrib['href'], rb.text))
            url = urllib.parse.urljoin(url, rb.attrib['href'])
            self.first_id = self.get_id_for_url(url)
            self.get_category(urllib.parse.urljoin(url, rb.attrib['href']))

    def get_category(self,url):
        '''
        获取分类
        :param url:一级分类的url
        :return:
        '''
        try:
            resp = fetch(url).text
        except RequestException as e:
            resp = fetch(url).text
            log.logging.info('[warn] ineffective:{0}'.format(e))
        html = etree.HTML(resp)
        childs = html.xpath('/html/body/div[4]/div[1]/div/a')

        for rc in childs[::-1]:
            log.logging.info('[INFO] Get url: {0} >>> {1}'.format(rc.attrib['href'], rc.text))
            url = urllib.parse.urljoin(url, rc.attrib['href'])
            url_join = url + "-" + self.first_id
            # 把url提取出来, 存到links.bin中
            if self.get_id_for_url(url): write_links(LINKS_BIN, url_join)
            # self.get_coupon_info(urllib.parse.urljoin(url, rc.attrib['href']), self.second_id)

    def get_coupon_info(self):
        '''
        获取商品信息
        :param url: 请求url
        :param self.second_id: 商品分类id
        :return:
        '''
        # 获取links.bin中的url
        urls = read_file_to_url(LINKS_BIN)
        for url in urls:
            m = url.replace("\n", "").split("-")
            url = m[0]
            first_id = m[1]
            second_id = self.get_id_for_url(url)
            page = 0
            while True:
                try:
                    resp = fetch(self.get_url.format(id=second_id, page=page))
                except RequestException as e:
                    resp = fetch(self.get_url.format(id=second_id, page=page))
                    log.logging.info('[warn] ineffective:{0}'.format(e))

                if resp.text[0] == "<" or len(resp.json().get('data')['coupon_list']) == CouponList.ZERO:
                    log.logging.info('[INFO] Get {0} success'.format(second_id))
                    break
                else:
                    if resp:
                        try:
                            if resp.json().get('data'):
                                log.logging.info('[INFO]page {0}'.format(page))
                                coupon = Coupon()
                                for info in resp.json().get('data')['coupon_list']:
                                    coupon.second_id = second_id
                                    coupon.first_id = first_id
                                    coupon.title = info['title']
                                    coupon.price = info['raw_price']
                                    coupon.url = info['url']
                                    coupon.thumbnail_pic = info['thumbnail_pic']
                                    if Goods.save_coupon(coupon):
                                        log.logging.info('[INFO] {0} save to database ok'.format(coupon.title))
                                    else:
                                        log.logging.info('[INFO] {0} is existed'.format(coupon.title))
                                page += 1
                            else:
                                log.logging.info('[ERROR] {0}'.format(resp.text))
                        except Exception as e:
                            log.logging.info('[ERROR] {0}'.format(e))
                    else:
                        log.logging.info('[ERROR] resp is None')
            # 一条url处理完成以后, 从文件中删除
            delete_line(LINKS_BIN, url)
import time

def start():
    start_time = time.time()

    if get_file_size(LINKS_BIN): BanTang().init_category()
    BanTang().get_coupon_info()
    log.logging.info('===============================================')
    log.logging.info('[INFO] Ibantang Ok time cost: {0}'.format(time.time() - start_time))
    log.logging.info('===============================================')
