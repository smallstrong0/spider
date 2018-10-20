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
from ss.spider_core import go
from ss.common.func import exe_time
from gevent import monkey, pool
import ss.config

monkey.patch_all()


@exe_time
def main():
    p = pool.Pool(ss.config.COROUTINE_LIMIT_NUM)
    while ss.config.FLAG:
        p.spawn(go)


if __name__ == '__main__':
    main()
