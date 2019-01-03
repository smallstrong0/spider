#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 22:08
# @Author  : SmallStrong
# @Des     : 
# @File    : spider_core.py
# @Software: PyCharm

import config
import random
import time


def go():
    """
    爬虫核心文件
    :return:
    """
    download()
    parser()
    pipeline()

    time.sleep(random.randint(0, 20) / 10.0)
    stop = random.randint(0, 200)
    print(stop)
    if stop == 150:
        set_process_end()


def download():
    pass


def parser():
    pass


def pipeline():
    pass


def set_process_end():
    config.FLAG = False
