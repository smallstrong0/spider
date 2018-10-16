#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 09:06
# @Author  : SmallStrong
# @Des     : 
# @File    : run.py
# @Software: PyCharm

import qinglong.download.ss_download as download
import qinglong.config as config
import killer.func as func
import qinglong.pipeline.export_to_output as export
import xuanwu.pipeline.export_to_redis as export_redis

redis_cli = export_redis.cli()


def go():
    tag_dic = {}
    index = 1
    while True:
        info = download.download(config.TAG_HOST + "{}/pageSize/40".format(index))
        s_info = func.deserialize(info)
        tag_list = s_info.get('d', {}).get('tags', [])
        if len(tag_list) > 0:
            for tag in tag_list:
                tag_dic[tag['id']] = tag
            index = index + 1
        else:
            break
    print(len(tag_dic))
    redis_cli.hmset('juejin_tag_dic', tag_dic)
    print('redis in ,ok!')


if __name__ == '__main__':
    go()
