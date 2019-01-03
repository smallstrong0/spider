#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 12:19
# @Author  : SmallStrong
# @Des     : 
# @File    : export_to_mongo.py
# @Software: PyCharm

from pymongo import MongoClient

MONGODB = {
    'HOST': 'localhost',
    'PORT': 27017,
    'DATABASE': 'db_name',
}


class cli:
    def __init__(self):
        client = MongoClient(host=MONGODB['HOST'], port=MONGODB['PORT'])
        self.db = client[MONGODB['DATABASE']]

    def insert(self, table_name, data):
        if self.db is None:
            return False
        else:
            collection = self.db[table_name]
            collection.insert(data)

    def insert_many(self, table_name, data_list):
        if self.db is None:
            return False
        else:
            collection = self.db[table_name]
            collection.insert_many(data_list)


def test():
    mongo_cli = cli()
    mongo_cli.insert('haha', data={'a': 1, 'b': 2})
    mongo_cli.insert_many('test', data_list=[{'a': 1, 'b': 2}, {'a': 1111, 'b': 22222}])


if __name__ == '__main__':
    test()
