#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 20:56
# @Author  : SmallStrong
# @Des     : 
# @File    : zhihu.py
# @Software: PyCharm

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  ###禁止提醒SSL警告


class Zhihu(object):
    def __init__(self, account, password):
        self.url = u'https://www.zhihu.com/api/v3/oauth/sign_in'
        self.account = account
        self.password = password
        self.session = requests.session()
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
            'Connection': 'Keep-Alive',
            'origin': 'https://www.zhihu.com',
            'Referer': 'https://www.zhihu.com/signup?next=%2F',
            'Pragma': 'no-cache',
            'Host': 'https://www.zhihu.com',
        }
        self.session.headers.update(headers)

    def download(self):  # 获取数据
        req = self.session.post(url=self.url, data=json.dumps({"phoneNumber": self.account, "password": self.password}),
                                verify=False)
        j = json.loads(req.text)
        self.parser(j)

    def parser(self, data):
        print(data)

    def closes(self):
        self.session.close()


if __name__ == '__main__':
    account = 18888888888
    password = u'password'
    zhihu = Zhihu(account=account, password=password)
    zhihu.download()
    zhihu.closes()