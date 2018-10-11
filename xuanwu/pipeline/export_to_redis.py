#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 00:07
# @Author  : SmallStrong
# @Des     : 
# @File    : export_to_redis.py
# @Software: PyCharm

import redis

import xuanwu.tool.config

NS = xuanwu.tool.config.NS


class cli:
    def __init__(self, mode=0):
        if mode == 0:
            # 连接本机redis服务
            self.__cli = redis.Redis()
        else:
            # 连接redis服务器（一般设置密码，且必须开启远程连接权限）
            self.__cli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, password='password')

    def exists(self, k):
        if self.__cli is None:
            return False
        else:
            return self.__cli.exists(NS + ':' + k)

    def get(self, k):
        if self.__cli is None:
            return None
        else:
            return self.__cli.get(NS + ':' + k)

    def hget(self, n, k):
        if self.__cli is None:
            return None
        else:
            return self.__cli.hget(NS + ':' + n, k)

    def hgetall(self, n):
        if self.__cli is None:
            return None
        else:
            return self.__cli.hgetall(NS + ':' + n)

    def hmset(self, n, mapping):
        if self.__cli is None:
            return None
        else:
            return self.__cli.hmset(NS + ':' + n, mapping)

    def hmget(self, n, k, *args):
        if self.__cli is None:
            return None
        else:
            return self.__cli.hmget(NS + ':' + n, k, *args)

    def hset(self, n, k, v):
        if self.__cli is None:
            return None
        else:
            return self.__cli.hset(NS + ':' + n, k, v)

    def hdel(self, n, *keys):
        if self.__cli is None:
            return None
        else:
            return self.__cli.hdel(NS + ':' + n, *keys)

    def mget(self, ks):
        if self.__cli is None:
            j = []
            for i in range(len(ks)):
                j.append(None)
            return j
        else:
            j = []
            for i in range(len(ks)):
                j.append(NS + ':' + ks[i])
            return self.__cli.mget(j)

    def zadd(self, n, *k, **v):
        if self.__cli is None:
            return False
        else:
            return self.__cli.zadd(NS + ':' + n, *k, **v)

    def zrem(self, n, *v):
        if self.__cli is None:
            return False
        else:
            return self.__cli.zrem(NS + ':' + n, *v)

    def zremrangebyscore(self, n, min, max):
        if self.__cli is None:
            return False
        else:
            return self.__cli.zremrangebyscore(NS + ':' + n, min, max)

    def zrange(self, n, start, end, desc=False, withscores=False, score_cast_func=float):
        if self.__cli is None:
            return False
        else:
            return self.__cli.zrange(NS + ':' + n, start, end, desc=desc, withscores=withscores,
                                     score_cast_func=score_cast_func)

    def zscore(self, n, *v):
        if self.__cli is None:
            return False
        else:
            return self.__cli.zscore(NS + ':' + n, *v)

    def zrevrange(self, n, start, end, withscores=False, score_cast_func=float):
        if self.__cli is None:
            return False
        else:
            return self.__cli.zrevrange(NS + ':' + n, start, end, withscores=withscores,
                                        score_cast_func=score_cast_func)

    def zrangebyscore(self, n, min, max, start=None, num=None, withscores=False, score_cast_func=float):
        if self.__cli is None:
            return False
        else:
            return self.__cli.zrangebyscore(NS + ':' + n, min, max, start=start, num=num,
                                            withscores=withscores, score_cast_func=score_cast_func)

    def zrank(self, n, v):
        if self.__cli is None:
            return False
        else:
            return self.__cli.zrank(NS + ':' + n, v)

    def zcount(self, n, min, max):
        if self.__cli is None:
            return False
        else:
            return self.__cli.zcount(NS + ':' + n, min, max)

    def zcard(self, n):
        if self.__cli is None:
            return False
        else:
            return self.__cli.zcard(NS + ':' + n)

    def set(self, k, v, t=86400 * 30):
        if self.__cli is None:
            return False
        else:
            if -1 == t:
                return self.__cli.set(NS + ':' + k, v)
            else:
                return self.__cli.set(NS + ':' + k, v, t)

    def delete(self, k):
        if self.__cli is None:
            return False
        else:
            return self.__cli.delete(NS + ':' + k)

    def incr(self, k):
        if self.__cli is None:
            return None
        else:
            return self.__cli.incr(NS + ':' + k)

    def setnx(self, k, v):
        if self.__cli is None:
            return False
        else:
            return self.__cli.setnx(NS + ':' + k, v)

    def getset(self, k, v):
        if self.__cli is None:
            return None
        else:
            return self.__cli.getset(NS + ':' + k, v)

    def decr(self, k):
        if self.__cli is None:
            return None
        else:
            return self.__cli.decr(NS + ':' + k)

    def expire(self, k, t):
        if self.__cli is None:
            return False
        else:
            return self.__cli.expire(NS + ':' + k, t)

    def expireat(self, k, w):
        if self.__cli is None:
            return False
        else:
            return self.__cli.expireat(NS + ':' + k, w)

    def ttl(self, k):
        if self.__cli is None:
            return -1
        else:
            return self.__cli.ttl(NS + ':' + k)

    def keys(self, pattern='*'):
        if self.__cli is None:
            return False
        else:
            return self.__cli.keys(pattern)

    def sadd(self, k, v, t=-1):
        if self.__cli is None:
            return False
        else:
            if -1 == t:
                return self.__cli.sadd(NS + ':' + k, v)
            else:
                return self.__cli.sadd(NS + ':' + k, v, t)

    def spop(self, k):
        if self.__cli is None:
            return False
        else:
            return self.__cli.spop(NS + ':' + k)

    def smembers(self, k):
        if self.__cli is None:
            return None
        else:
            return self.__cli.smembers(NS + ':' + k)

    def srem(self, k):
        if self.__cli is None:
            return None
        else:
            return self.__cli.srem(NS + ':' + k)

    def pfadd(self, n, *k):
        if self.__cli is None:
            return False
        else:
            return self.__cli.pfadd(NS + ':' + n, *k)

    def pfcount(self, n):
        if self.__cli is None:
            return False
        else:
            return self.__cli.pfcount(NS + ':' + n)
