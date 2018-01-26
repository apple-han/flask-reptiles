#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
再次感谢半塘提供数据支持
'''
import urllib
import random
import json
import requests
from lxml import etree

from requests.exceptions import RequestException

from public.base_spider import BaseSpider
from public import log
from public.model import Coupon
from public.db.coupon_db import CouponDB
from public.settings import REFERER_LIST
from util.getIp import fetch


class BanTang(BaseSpider):
    def __init__(self):
        super(BanTang,self).__init__()
        self.site_url = 'http://www.ibantang.com/g/14/'
        log.logging.info('[INFO] ============================================')
        log.logging.info('[INFO] Start site: {0}'.format(self.site_url))
        self.get_url = 'http://www.ibantang.com/g/getProductList?id={id}&sort=0&page={page}&pagesize=20'

    def get_random_ip(self):
        return random.choice(CouponDB().sumip())['ip']

    def init_category(self):
        '''
        获取所有的一级分类
        :return:
        '''
        log.logging.info('[INFO] Get category')
        url = self.site_url
        try:
            res = fetch(url, proxy=self.get_random_ip()).text()
        except RequestException as e:
            res = fetch(url).text()
            log.logging.info('[warn] ineffective:{0}'.format(e))
        html = etree.HTML(res)
        # 一级分类
        root_brother = html.xpath("/html/body/div[2]/div[2]/div[1]/a")
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
        time.sleep(10)
        try:
            resp = fetch(url, proxy=self.get_random_ip()).text()
        except RequestException as e:
            resp = fetch(url).text()
            log.logging.info('[warn] ineffective:{0}'.format(e))
        html = etree.HTML(resp)
        childs = html.xpath('/html/body/div[2]/div[2]/div[2]/div/a')

        for rc in childs[::-1]:
            log.logging.info('[INFO] Get url: {0} >>> {1}'.format(rc.attrib['href'], rc.text))
            url = urllib.parse.urljoin(url, rc.attrib['href'])
            self.second_id = self.get_id_for_url(url)
            self.get_category_second(urllib.parse.urljoin(url, rc.attrib['href']))


    def get_category_second(self,url):
        '''
        三级分类
        :param url:
        :return:
        '''
        time.sleep(10)
        try:
            resp = fetch(url, proxy=self.get_random_ip()).text()
        except RequestException as e:
            resp = fetch(url).text()
            log.logging.info('[warn] ineffective:{0}'.format(e))
        html = etree.HTML(resp)
        childs = html.xpath('/html/body/div[2]/div[2]/div[3]/div/a')

        for child in childs[::-1]:
            result_url = urllib.parse.urljoin(url, child.attrib['href'])
            cate_id = self.get_id_for_url(result_url)
            self.get_coupon_info(result_url,cate_id)


    def get_coupon_info(self, url,cate_id):
        '''
        获取商品信息
        :param url: 请求url
        :param cate_id: 商品分类id
        :return:
        '''

        page = 0
        while True:
            time.sleep(10)
            try:
                resp = fetch(self.get_url.format(id=cate_id, page=page), proxy=self.get_random_ip())
            except RequestException as e:
                resp = fetch(self.get_url.format(id=cate_id, page=page))
                log.logging.info('[warn] ineffective:{0}'.format(e))
            time.sleep(10)
            try:
                resp2 = fetch(self.get_url.format(id=cate_id, page=page+1),proxy=self.get_random_ip())
            except RequestException as e:
                resp2 = fetch(self.get_url.format(id=cate_id, page=page+1))
                log.logging.info('[warn] ineffective:{0}'.format(e))

            if resp.text() == resp2.text():
                log.logging.info('[INFO] Get {0} success'.format(cate_id))
                break
            else:
                if resp:
                    try:
                        if json.loads(resp.text()).get('data'):
                            log.logging.info('[INFO]page {0}'.format(page,))
                            coupon = Coupon()
                            for info in json.loads(resp.text()).get('data')['product']:
                                coupon.category_id = cate_id
                                coupon.second_id = self.second_id
                                coupon.first_id = self.first_id
                                coupon.title = info['title']
                                coupon.price = info['price']
                                coupon.url = info['url']
                                coupon.pic = info['pic']
                                coupon.goods_desc = info['desc']
                                coupon.brand = info['brand']['name']
                                coupon.add_time = self.timestamp_to_date_str(self.get_time_now())
                                print(info['title'])
                                if self.coupon_db.save_coupon(coupon):
                                    log.logging.info('[INFO] {0} save to database ok'.format(coupon))
                                else:
                                    log.logging.info('[INFO] {0} is existed'.format(coupon))
                            page += 1
                        else:
                            log.logging.info('[ERROR] {0}'.format(resp.text()))
                    except Exception as e:
                        log.logging.info('[ERROR] {0}'.format(e))
                else:
                    log.logging.info('[ERROR] resp is None')
import time

def start():
    start_time = time.time()
    BanTang().init_category()
    log.logging.info('===============================================')
    log.logging.info('[INFO] Ibantang Ok time cost: {0}'.format(time.time() - start_time))
    log.logging.info('===============================================')
