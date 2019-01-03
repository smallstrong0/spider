#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 21:58
# @Author  : SmallStrong
# @Des     : 
# @File    : run.py
# @Software: PyCharm

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
import os_mul_process as speed
import config


def go():
    for i in range(config.PROCESS_LIMIT_NUM):
        speed.dash(os.getcwd() + '/download/ss_coroutine.py', '{}_{}'.format(config.LOG_FILE_NAME, i))


if __name__ == '__main__':
    go()
