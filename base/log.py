#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging.config

import datetime
from logging.handlers import RotatingFileHandler

from config.config import CONFIG_DIR


def start_log(file_path):
    this_time = datetime.datetime.now()
    result_day = []
    for arg in ('year', 'month', 'day'):
        result_day.append('{}'.format(getattr(this_time, arg)))

    log_path = os.path.join(
        CONFIG_DIR, "log" + os.sep + file_path +
                   os.sep + str(result_day[0]) +
                   os.sep + str(result_day[1]))

    if not os.path.exists(log_path):
        os.makedirs(log_path)

    logging_conf_file = os.path.join(log_path, str(result_day[2]) + ".log")
    format = logging.Formatter('%(asctime)s %(pathname)s [line:%(lineno)d] %(levelname)s %(message)s')
    level = logging.INFO

    log = logging.getLogger()
    handler = RotatingFileHandler(logging_conf_file, maxBytes=1024 * 1024 * 1024, backupCount=40)
    handler.setFormatter(format)

    log.addHandler(handler)
    log.setLevel(level)
