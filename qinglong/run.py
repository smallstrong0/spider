#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 09:06
# @Author  : SmallStrong
# @Des     : 
# @File    : run.py
# @Software: PyCharm

import sys
import os
import traceback
import qinglong.download.ss_download as download
import qinglong.config as config
import ss.common.func as func
import qinglong.pipeline.export_to_redis as export_redis

redis_cli = export_redis.cli()


def get_content_list():
    """
    获取所有列表内容
    :return:
    """

    try:
        while True:
            _id = redis_cli.spop('tag_set')
            redis_cli.sadd('tag_set', _id)
            print(_id)
            index = 1
            if _id:
                while True:
                    info = download.download(
                        config.CONTENT_LIST_HOST + "src=web&tagId={}&page={}&pageSize=20&sort=rankIndex".format(
                            _id, index))
                    s_info = func.deserialize(info)
                    if type(s_info) == dict:
                        temp_dic = s_info.get('d', {})
                        if type(temp_dic) == dict:
                            entry_list = s_info.get('d', {}).get('entrylist', [])
                            if len(entry_list) > 0:
                                result_dic = {}
                                for entry in entry_list:
                                    originalUrl = entry.get('originalUrl', '')
                                    if originalUrl:
                                        result_dic[originalUrl] = func.serialize(entry)
                                if result_dic:
                                    redis_cli.hmset(_id, result_dic)
                                index = index + 1
                            else:
                                redis_cli.srem('tag_set', _id)
                                break
                        else:
                            print('2：数据结构有误')
                            print(temp_dic)
                            redis_cli.srem('tag_set', _id)
                            break
                    else:
                        print('1：数据结构有误')
                        print(s_info)
                        redis_cli.srem('tag_set', _id)
                        break
            else:
                break
    except Exception as e:
        print >> sys.stderr, func.get_time()
        traceback.print_exc()
        sys.stderr.flush()


def get_all_tags():
    """
    获取所有标签
    :return:
    """
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

    all_tags = redis_cli.hgetall('juejin_tag_dic')
    for tag in all_tags:
        redis_cli.sadd('tag_set', tag)


def cal():
    """
    数据统计
    没有文章的标签数量=195
    文章总数=134150
    :return:
    """
    all_tags = redis_cli.hgetall('juejin_tag_dic')
    i = 0
    sum_num = 0
    for tag in all_tags:
        data = redis_cli.hgetall(tag)
        if not data:
            i = i + 1
            print(tag)
        else:
            sum_num = sum_num + len(data)
    print('没有文章的标签数量={}'.format(i))
    print('文章总数={}'.format(sum_num))


if __name__ == '__main__':
    """
    按步骤进行一个个跑  第二步能用mul_run加速
    """
    get_all_tags()
    get_content_list()
    cal()
