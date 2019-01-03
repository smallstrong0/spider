#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 08:37
# @Author  : SmallStrong
# @Des     : 系统级别的多进程任务
# @File    : os_mul_process.py
# @Software: PyCharm

import os
import config

PROCESS_LIMIT_NUM = config.PROCESS_LIMIT_NUM


def check_process_num(process_name, limit_num=PROCESS_LIMIT_NUM):
    """
    检查进程数是否超标
    :param process_name:
    :param limit_num:
    :return:
    """

    num = long(os.popen(
        'ps aux | grep "' + process_name + '" | grep -v grep | wc -l').read().strip())
    print 'current process num {}'.format(num)
    if num >= limit_num:
        return False
    return True


def dash(file_path, log_file_name):
    """
    启动后台进程  可配合for循环实现系统级别的多进程
    :param file_path:
    :param log_file_name:
    :return:
    """
    cmd = 'nohup python {}  1>>{}.log 2>>{}.err &'.format(file_path, os.getcwd() + '/log/output/' + log_file_name,
                                                          os.getcwd() + '/log/output/' + log_file_name)
    os.system(cmd)
