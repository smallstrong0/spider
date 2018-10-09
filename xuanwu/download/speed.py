#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 08:37
# @Author  : SmallStrong
# @Des     : 
# @File    : speed.py
# @Software: PyCharm

import os
import time

PROCESS_LIMIT_NUM = 10
PATH = ''


def go():
    for i in xrange(40, 175):
        exec 'import ' + 'pk_{}'.format(i)
        ID_LIST = eval('pk_{}'.format(i)).ID_LIST
        while not _add_process(PROCESS_LIMIT_NUM):
            time.sleep(1)
        dash(ID_LIST)


def _add_process(process_name, limit_num=PROCESS_LIMIT_NUM):
    num = long(os.popen(
        'ps aux | grep "' + process_name + '" | grep -v grep | wc -l').read().strip())
    print 'current process num {}'.format(num)
    if num >= limit_num:
        return False
    return True


def dash(path, log_file_name):
    cmd = 'nohup python {}  1>>{}.log 2>>{}.err &'.format(path, log_file_name, log_file_name)
    os.system(cmd)
