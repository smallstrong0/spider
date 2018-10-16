#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 23:15
# @Author  : SmallStrong
# @Des     : 
# @File    : export_to_output.py
# @Software: PyCharm

import ss.common.func as func


def write(file_name, data_name, data):
    f = open("./pipeline/output/{}.py".format(file_name), 'w+')
    print >> f, '# !/bin/python'
    print >> f, '# -*- coding: utf8 -*-'
    print >> f, '{} = {}'.format(data_name, func.sort_serialize(data))
