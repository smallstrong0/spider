#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 15:39
# @Author  : SmallStrong
# @Des     : 
# @File    : proxy.py
# @Software: PyCharm


import requests


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
