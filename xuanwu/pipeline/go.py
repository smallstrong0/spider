#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 12:43
# @Author  : SmallStrong
# @Des     : 
# @File    : go.py
# @Software: PyCharm
import xuanwu.pipeline.export_to_redis as export_redis
import xuanwu.pipeline.export_to_output as export
import uuid
import json

redis_cli = export_redis.cli()


def go():
    category_dic = redis_cli.hgetall('category_dic')
    export.write('category_dic', 'category_dic', category_dic)

    recipe_dic = redis_cli.hgetall('recipe_dic')
    export.write('recipe_dic', 'recipe_dic', recipe_dic)

    result_list = []
    _list = redis_cli.keys('xcf:/recipe/*')
    print(len(_list))
    for i in _list:
        while len(result_list) >= 1000:
            export.write(str(uuid.uuid1()), 'result_list', result_list)
            result_list = []
        result_list.append(redis_cli.hgetall(i.split('xcf:')[1]))
    export.write(str(uuid.uuid1()), 'result_list', result_list)


if __name__ == '__main__':
    go()
