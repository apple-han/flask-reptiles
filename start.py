# -*- coding: utf-8 -*-
__author__ = 'Apple'
import os
import re
import time
from public import log


# 启动日志
log.start_log(file_path="task")
log.logging.info('[INFO Start Time Task.]')


PYTHONPATH = "python"
# 定时任务几点执行
RUN_TIME = 0
# 多少秒检查一次是否到指定的时间
SLEEP_TIME = 1800
# 是否获取了新数据，以此来决定是否运行分词系统
NEW_DATA = False


# 执行系统命令并获取结果
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


while True:
    sys_ps = execCmd('ps -ef | grep python')
    log.logging.info("[INFO] System Process: ")
    log.logging.info(sys_ps)
    current_time = time.localtime(time.time())
    this_time_hour = current_time.tm_hour
    # 检查半糖爬虫是否在运行
    taobao = re.search(r'start_bantang\.py', sys_ps)
    participle = re.search(r'start_participle\.py', sys_ps)
    if RUN_TIME <= this_time_hour <= (RUN_TIME + 1):

        if not taobao:
            log.logging.info('[INFO] Run start_dataoke')
            os.popen("{0} start_bantang.py &".format(PYTHONPATH))
        if not participle:
            log.logging.info('[INFO] Run start_participle')
            os.popen("{0} start_participle.py &".format(PYTHONPATH))

    log.logging.info('[INFO] SLEEP {0}'.format(SLEEP_TIME))
    time.sleep(SLEEP_TIME)

