import time
from multiprocessing import Process
from base.proxypool.api import app
from base.proxypool.getter import Getter
from base.proxypool.tester import Tester
from base.proxypool.db import RedisClient
from base.proxypool.setting import *


class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)
    
    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)
    
    def schedule_api(self):
        """
        开启API
        """
        app.run(API_HOST, API_PORT)
    
    def run(self):
        print('代理池开始运行')
        
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        
        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
