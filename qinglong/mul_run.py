#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 15:02
# @Author  : SmallStrong
# @Des     : 
# @File    : mul_run.py
# @Software: PyCharm


import os
import qinglong.download.speed as speed


def go():
    for i in range(speed.PROCESS_LIMIT_NUM):
        speed.dash(os.getcwd() + '/run.py', 'juejin')


if __name__ == '__main__':
    go()