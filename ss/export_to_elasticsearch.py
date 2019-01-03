#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 11:33
# @Author  : SmallStrong
# @Des     :
# 参考 https://elasticsearch-py.readthedocs.io/en/master/index.html
# @File    : export_to_elasticsearch.py
# @Software: PyCharm

from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch()


def write_to_elastic(data, index='default_db', doc_type='default_table', _id=None):
    res = es.index(index=index, doc_type=doc_type, id=_id, body=data)
    print(res['result'])


def get_from_elastic(index='default_db', doc_type='default_table', _id=None):
    if not _id:
        return
    res = es.get(index=index, doc_type=doc_type, id=_id)
    print(res['_source'])


def test():
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
    print(res['result'])

    res = es.get(index="test-index", doc_type='tweet', id=1)
    print(res['_source'])

    es.indices.refresh(index="test-index")

    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


if __name__ == '__main__':
    # test()
    write_to_elastic({'a': 1, 'b': 2}, _id=222)
    write_to_elastic({'a': 1, 'b': 2}, index='small_db', doc_type='test', _id=222)
