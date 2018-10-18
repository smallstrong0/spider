#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 21:58
# @Author  : SmallStrong
# @Des     : 
# @File    : run.py
# @Software: PyCharm

import os
import ss.download.os_mul_process as speed
import config


def go():
    for i in range(config.PROCESS_LIMIT_NUM):
        speed.dash(os.getcwd() + '/download/ss_coroutine.py', config.LOG_FILE_NAME)


if __name__ == '__main__':
    go()
