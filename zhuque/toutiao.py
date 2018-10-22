#!coding=utf-8
##爬取今日头条频道数据
import requests
import re
import json
import math
import random
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pandas as pd

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  ###禁止提醒SSL警告
# requests.packages.urllib3.disable_warnings()
import hashlib
import execjs
import toutiao_core


class toutiao(object):
    def __init__(self, path, url):
        self.path = path  # CSV保存地址
        self.url = url
        self.s = requests.session()
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
            'Connection': 'Keep-Alive',
        }
        self.s.headers.update(headers)
        self.channel = re.search('ch/(.*?)/', url).group(1)

    def getdata(self):  # 获取数据
        headers = {'referer': self.url}
        max_behot_time = '0'
        self.s.headers.update(headers)
        for i in range(0, 30):
            sign_params = json.loads(toutiao_core.get_sign_params())
            eas = sign_params['as']
            ecp = sign_params['cp']
            signature = sign_params['_signature']
            url = 'https://www.toutiao.com/api/pc/feed/?category={}&utm_source=toutiao&widen=1&max_behot_time={}&max_behot_time_tmp={}&tadrequire=true&as={}&cp={}&_signature={}'.format(
                self.channel, max_behot_time, max_behot_time, eas, ecp, signature)
            req = self.s.get(url=url, verify=False)
            time.sleep(random.random() * 2 + 2)
            j = json.loads(req.text)
            self.parser(j)

    def parser(self, j):
        title = []
        source = []
        source_url = []
        comments_count = []
        tag = []
        chinese_tag = []
        label = []
        abstract = []
        behot_time = []
        nowtime = []
        duration = []
        for k in range(0, 10):
            now = time.time()
            if j['data'][k]['tag'] != 'ad':
                title.append(j['data'][k]['title'])  ##标题
                source.append(j['data'][k]['source'])  ##作者
                source_url.append('https://www.toutiao.com/' + j['data'][k]['source_url'])  ##文章链接
                try:
                    comments_count.append(j['data'][k]['comments_count'])  ###评论
                except:
                    comments_count.append(0)

                tag.append(j['data'][k]['tag'])  ###频道名
                try:
                    chinese_tag.append(j['data'][k]['chinese_tag'])  ##频道中文名
                except:
                    chinese_tag.append('')
                try:
                    label.append(j['data'][k]['label'])  ## 标签
                except:
                    label.append('')
                try:
                    abstract.append(j['data'][k]['abstract'])  ###文章摘要
                except:
                    abstract.append('')
                behot = int(j['data'][k]['behot_time'])
                behot_time.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(behot)))  ####发布时间
                nowtime.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now)))  ##抓取时间
                duration.append(now - behot)  ##发布时长
                data = {'title': title, 'source': source, 'source_url': source_url, 'comments_count': comments_count,
                        'tag': tag,
                        'chinese_tag': chinese_tag, 'label': label, 'abstract': abstract, 'behot_time': behot_time,
                        'nowtime': nowtime, 'duration': duration,
                        }
                print(data)

    def closes(self):
        self.s.close()


if __name__ == '__main__':
    path = r'./'  ##保存路径
    url = 'https://www.toutiao.com/ch/news_tech/'  ##频道URL
    t = toutiao(path, url)
    t.getdata()
    t.closes()
