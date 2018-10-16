#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 上午9:24
# @Author  : SmallStrong
# @Des     : 网页下载
# @File    : ss_download.py
# @Software: PyCharm

import urllib2
import urlparse
import ss.download.http.ua_list as ua_list
from random import choice
import ss.config as config
import ss.download.http.proxy as proxy_tool
import time


def download(url, proxy=proxy_tool.get_proxy(), num_retries=config.NUM_RETRIES):
    """
    :param url: 网址链接
    :param user_agent: 用户代理
    :param proxy: 设置代理
    :param num_retries: 下载错误重新下载次数
    :return:
    """
    time.sleep(config.DELAY)
    print 'Downloading:{}'.format(url)
    headers = {
        'User-agent': choice(ua_list.UA_LIST),
    }
    request = urllib2.Request(url, headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:{}'.format(e)
        if proxy:
            proxy_tool.delete_proxy(proxy)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 400 <= e.code < 600:
                return download(url, choice(ua_list.UA_LIST), num_retries - 1)
    return html
