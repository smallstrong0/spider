#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 23:15
# @Author  : SmallStrong
# @Des     : 
# @File    : export_to_output.py
# @Software: PyCharm

import sys
import json


def write(file_name, data_name, data):
    f = open("./pipeline/output/{}.py".format(file_name), 'w+')
    print >> f, '# !/bin/python'
    print >> f, '# -*- coding: utf8 -*-'
    print >> f, '{} = {}'.format(data_name, sort_serialize(data))


def sort_serialize(data):
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    try:
        return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
    except Exception as e:
        return None
