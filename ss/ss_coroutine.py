#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 22:07
# @Author  : SmallStrong
# @Des     : 
# @File    : ss_coroutine.py
# @Software: PyCharm
import sys
import os

# 被逼无奈
sys.path.append(os.getcwd().replace('/ss', ''))
from spider_core import go
from func import exe_time
from gevent import monkey, pool
import config

monkey.patch_all()


@exe_time
def main():
    p = pool.Pool(config.COROUTINE_LIMIT_NUM)
    while config.FLAG:
        p.spawn(go)


if __name__ == '__main__':
    main()
