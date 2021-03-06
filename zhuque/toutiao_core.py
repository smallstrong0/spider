#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/21 21:18
# @Author  : SmallStrong
# @Des     : 
# @File    : toutiao_core.py
# @Software: PyCharm

import os
import math
import time
import hashlib
import json
import execjs


def get_sign_params():
    f = open(r"{}/sign.js".format(os.getcwd()), 'r')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    ctx = execjs.compile(htmlstr)
    return ctx.call('get_as_cp_signature')


def get_as_cp():
    t = int(math.floor(time.time()))
    e = hex(t).upper()[2:]
    m = hashlib.md5()
    m.update(str(t).encode(encoding='utf-8'))
    i = m.hexdigest().upper()

    if len(e) != 8:
        AS = '479BB4B7254C150'
        CP = '7E0AC8874BB0985'
        return AS, CP
    n = i[0:5]
    a = i[-5:]
    s = ''
    r = ''
    for o in range(5):
        s += n[o] + e[o]
        r += e[o + 3] + a[o]

    AS = 'A1' + s + e[-3:]
    CP = e[0:3] + r + 'E1'
    return AS, CP
