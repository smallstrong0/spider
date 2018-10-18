#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 18:16
# @Author  : SmallStrong
# @Des     : 
# @File    : config.py
# @Software: PyCharm

import random

DELAY = 0.5 + random.random()  # 爬虫延时
NUM_RETRIES = 5  # 链接重试次数
NS = 'ss'  # redis缓存前缀
PROCESS_LIMIT_NUM = 10  # 开多少进程数量
COROUTINE_LIMIT_NUM = 10  # 单进程开启协程的数量
FLAG = True  # 进程是否开启的标志
LOG_FILE_NAME = 'test'  # 日志文件名
