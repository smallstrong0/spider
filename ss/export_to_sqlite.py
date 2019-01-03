#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 09:49
# @Author  : SmallStrong
# @Des     : 参考 https://www.cnblogs.com/zknublx/p/8710110.html
# @File    : export_to_sqlite.py
# @Software: PyCharm

from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import logging
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean, Unicode, SmallInteger, BigInteger, Numeric, Float, DateTime, \
    Date, Time, \
    Binary, LargeBinary

SQLITE = {
    'PATH': '/Users/smallstrong/Desktop',
    'DATABASE': 'small',
}

Base = declarative_base()

conn = 'sqlite:////{}/{}.db'.format(SQLITE['PATH'], SQLITE['DATABASE'])  # PATH是sqlite db的绝对路径
engine = create_engine(conn, pool_size=10, pool_recycle=500, pool_timeout=30, pool_pre_ping=True, max_overflow=0,
                       poolclass=QueuePool)
Session = sessionmaker(bind=engine)


class cli:
    def __init__(self):
        self.session = Session()

    def con_commit_close(self, func):
        def wrapper(*args, **kw):
            try:
                func(*args, **kw)
                self.session.commit()
            except Exception as e:
                self.session.rollback()
                logging.error(e.message)
            finally:
                self.session.close()

        return wrapper


def test(bean):
    rds = cli()
    session = rds.session
    session.add(bean)
    session.commit()


############################
# 数据结构与建表
############################
class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    name = Column(String(20))


def create_table():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_table()
    test(User(user_id=12231, name='small'))
