#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 18:31
# @Author  : SmallStrong
# @Des     : 开启系统多进程爬取
# @File    : mul_go.py
# @Software: PyCharm

import os
import xuanwu.download.speed as speed


def go():
    for i in range(speed.PROCESS_LIMIT_NUM):
        speed.dash(os.getcwd() + '/go.py', 'xcf')


if __name__ == '__main__':
    go()
