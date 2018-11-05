#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 00:26
# @Author  : SmallStrong
# @Des     : 
# @File    : juejin.py
# @Software: PyCharm

import requests
import re
import json
import math
import random
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  ###禁止提醒SSL警告


class JueJin(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.session()
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
            'Connection': 'Keep-Alive',
        }
        self.s.headers.update(headers)

    def download(self):  # 获取数据
        headers = {'referer': self.url}
        self.session.headers.update(headers)
        url = ''
        req = self.session.get(url=url, verify=False)
        j = json.loads(req.text)
        self.parser(j)

    def parser(self, data):
        pass

    def closes(self):
        self.session.close()


if __name__ == '__main__':
    url = u'https://juejin.im/auth/type/phoneNumber'
    juejin = JueJin(url=url)
    juejin.download()
