#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging.config
import datetime
from public.settings import CONFIG_DIR

def start_log(file_path):
    this_time = datetime.datetime.now()
    result_day = []
    for arg in ('year','month','day'):
        result_day.append('{}'.format(getattr(this_time,arg)))

    log_path = os.path.join(CONFIG_DIR, "log" + os.sep + file_path + os.sep + str(result_day[0]) + os.sep + str(result_day[1]))

    if not os.path.exists(log_path):
        os.makedirs(log_path)

    LOGGING_CONF_FILE = os.path.join(log_path, str(result_day[2]) + ".log")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(pathname)s [line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename=LOGGING_CONF_FILE,
        filemode='a'
    )
