#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 09:24
# @Author  : SmallStrong
# @Des     :
# @File    : ua_maker.py
# @Software: PyCharm

import requests as req
from bs4 import BeautifulSoup
import time
import sys
import json

result_list = []
lst = ['Firefox', 'Internet+Explorer', 'Opera', 'Safari', 'Chrome', 'Edge', 'Android+Webkit+Browser']


def getUa(br):
    url = 'http://www.useragentstring.com/pages/useragentstring.php?name=' + br
    r = req.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
    else:
        soup = False

    if soup:
        div = soup.find('div', {'id': 'liste'})
        lnk = div.findAll('a')

        for i in lnk:
            try:
                if '-->>' not in i.text and i.text not in ["Google", "Chrome"]:
                    result_list.append(i.text)
                # save(br, i.text)
            except:
                print 'no ua'
    else:
        print 'No soup for ' + br


def sort_serialize(data):
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    try:
        return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
    except Exception as e:
        # print e
        return None


def pr(data):
    f = open("./ua_list.py", 'w+')
    print >> f, '# !/bin/python'
    print >> f, '# -*- coding: utf8 -*-'
    print >> f, 'UA_LIST = {}'.format(sort_serialize(data))


if __name__ == '__main__':
    for i in lst:
        getUa(i)
        time.sleep(1)
    pr(result_list)
