#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 09:24
# @Author  : SmallStrong
# @Des     : 
# @File    : go.py
# @Software: PyCharm

import os
import time
import download.ss_download as download
import parser.xcf_parser as parser
import xuanwu.pipeline.export_to_redis as export_redis
import xuanwu.download.speed as speed

redis_cli = export_redis.cli()

BASE_URL = 'http://m.xiachufang.com'
WEB_BASE_URL = 'https://xiachufang.com'
CATEGORY_URL = 'https://www.xiachufang.com/category/'


def get_category():
    """
    获取分类
    :return:
    """
    content = download.download(CATEGORY_URL)
    parser.get_category_dic(content)


def get_recipe():
    """
    redis获取分类 分页爬完置1
    :return:
    """
    all_category_dic = redis_cli.hgetall('category_dic')
    for category in all_category_dic:
        if all_category_dic[category] == '0':
            for i in xrange(1, 100):
                category_list_content = download.download(BASE_URL + category + '?page={}'.format(i))
                if category_list_content:
                    recipe_dic = parser.get_recipe_list(category_list_content)
                    if not recipe_dic:
                        redis_cli.hset('category_dic', category, '1')
                        break
                else:
                    redis_cli.hset('category_dic', category, '1')
                    break
        else:
            pass


def get_content():
    # all_recipe_dic = redis_cli.hgetall('recipe_dic')
    # for recipe in all_recipe_dic:
    #     redis_cli.sadd('recipe_set', recipe)

    while 1:
        recipe = redis_cli.spop('recipe_set')
        if recipe:
            dish_content = download.download(BASE_URL + recipe)
            if dish_content:
                content_dic, error = parser.get_content(dish_content)
                if error is None:
                    redis_cli.hmset(recipe, content_dic)
                else:
                    redis_cli.hmset(recipe, content_dic)
            else:
                redis_cli.hmset('error' + recipe, {})
        else:
            break


def go():
    # get_category()
    # get_recipe()
    get_content()


if __name__ == '__main__':
    go()
