#! /usr/bin/env python
# -*- coding: utf8 -*-

import time
import datetime
import json
import random
import hashlib
import math
import uuid
import HTMLParser
import calendar
import urllib
import string
import sys
import re
import copy


def exe_time(func):
    """
    函数耗时装饰器
    :param func:
    :return:
    """

    def wrapper(*args, **args2):
        t0 = time.time()
        print "@%s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__)
        back = func(*args, **args2)
        print "@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__)
        print "@%.3fs taken for {%s}" % (time.time() - t0, func.__name__)
        return back

    return wrapper


def expire_time():
    '''
    装饰器函数, 检测程序耗时
    :return:
    '''

    def wrapper(func):
        # *args表示元祖参数，**kwargs
        def time_calc(*args, **kwargs):
            t0 = time.time()
            back = func(*args, **kwargs)
            t1 = time.time()
            if (t1 - t0) * 1000 > 100:
                print "@%d ms taken for {%s} param {%s} {%s}" % ((t1 - t0) * 1000, func.__name__, args, kwargs)
                # logger.info("@%d ms taken for {%s} param {%s} {%s}" % ((t1-t0)*1000, func.__name__,args,kwargs))
            return back

        return time_calc

    return wrapper


def decode_html(s):
    return HTMLParser.HTMLParser().unescape(s)


def serialize(data):
    try:
        return json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    except Exception as e:
        # print e
        return None


def sort_serialize(data):
    """
    对字典进行排序 记录打印的地方
    :param data:
    :return:
    """

    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back

    print '%s, %s, %s, %s, ' % (str(get_day()), f.f_code.co_filename, f.f_code.co_name, str(f.f_lineno))

    try:
        return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
    except Exception as e:
        # print e
        return None


def check_sort_serialize(data=None, msg=None):
    '''data传一个字典过来, msg传错误信息。两者不兼容！！！，有data不传msg,有msg不穿data'''
    if msg is not None and len(msg) > 0:  # 说明有错误
        return sort_serialize({"data": {}, "code": -1, "message": msg})
    elif msg is None and data is not None:
        return sort_serialize({"data": data, "code": 200, "message": "ok"})


def deserialize(data):
    try:
        return json.loads(data)
    except Exception as e:
        # print e
        return None


def random_string(length=16):
    s = ''
    for i in range(length):
        s += chr(random.randint(33, 126))
    return s


def guid():
    return str(uuid.uuid1())


def guid32():
    return str(uuid.uuid1()).replace('-', '')


def hash(plain):
    return hashlib.sha1(plain).hexdigest()


def get_ts():
    return long(time.time())


def get_ms():
    return long(time.time() * 1000)


def day2ts(day):
    """
    :param day: 2017-09-09
    :return: 时间轴
    """
    return time.mktime(time.strptime(day, '%Y-%m-%d'))


def month2ts(month):
    return int(time.mktime(time.strptime(month, '%Y/%m')))


# please don't change get_day() 's time format if you want to change , notice JoshuaR
def get_day(ts=None):
    if ts is None:
        ts = get_ts()
    return time.strftime('%Y-%m-%d', time.localtime(ts))


# *****************************************

def get_week_num():
    '''
    获取今天的星期
    :return: 0~6,0->Sunday
    '''
    l_time = time.localtime()
    return int(time.strftime('%w', l_time))


def get_day_cn(ts=None):
    if ts is None:
        ts = get_ts()
    return time.strftime('%Y年%m月%d日', time.localtime(ts))


def get_interview_time(ts=None, time_format=None):
    if ts is None:
        ts = get_ts()
    if time_format == 'time':
        return time.strftime('%H:%M', time.localtime(ts))
    return time.strftime('%Y-%m-%d  %H:%M', time.localtime(ts))


def get_min_hour_time(ts=None):
    if ts is None:
        ts = get_ts()
    return time.strftime('%Y-%m-%d  %H', time.localtime(ts))


def get_timestamp_with_time(now_time, time_format):
    time_array = time.strptime(str(now_time), time_format)
    timestamp = time.mktime(time_array)
    return long(timestamp)


def get_time(ts=None):
    if ts is None:
        ts = get_ts()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))


def get_wx_time(ts=None):
    if ts is None:
        ts = get_ts()
    return time.strftime("%Y%m%d%H%M%S", time.localtime(ts))


def get_microtime():
    return long(time.time()) * 1000 * 1000 + datetime.datetime.now().microsecond


def get_today_zero_time():
    return day2ts(get_day())


def pagination(items, page_num, page_size):
    num_entries = len(items)
    page_max = int(math.ceil(float(num_entries) / page_size))
    if page_num < 1:
        page_num = 1
    if page_num > page_max:
        page_num = page_max
    return items[(page_num - 1) * page_size: page_num * page_size], page_num, page_max, num_entries


def get_last_month(date=None):
    if not date:
        date = get_day()
    date_list = date.split('-')
    if int(date_list[1]) == 1:
        return '{}-12'.format(int(date_list[0]) - 1)

    return '{}-{}'.format(date_list[0], str(int(date_list[1]) - 1).zfill(2))


def get_week_first_day(ts=None):
    if not ts:
        ts = get_ts()
    day = get_day(ts)
    time_list = day.split('-')
    week = calendar.weekday(int(time_list[0]), int(time_list[1]), int(time_list[2]))
    week_first_day = get_day(ts - week * 86400)
    return week_first_day


def get_week_first_timestamp(ts=None):
    a = '{} 00:00:01'.format(get_week_first_day(ts))
    s = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
    return long(s)


def time_sleep(s=0.02):
    time.sleep(s)


def get_day_first_time(times, time_format='%Y-%m-%d'):
    timeArray = time.strptime(times, time_format)
    return long(time.mktime(timeArray))


def get_month(ts=None):
    if ts is None:
        ts = get_ts()
    return time.strftime('%Y-%m', time.localtime(ts))


def md5(src):
    m2 = hashlib.md5()
    m2.update(src)
    return m2.hexdigest()


def get_each_time(ts=None, type='d'):
    '''
    输入时间戳与类型，返回字符串格式
    :param ts:
    :param type:{str} 根据不同的类型返回不同格式的时间字符串
    :return:{str}
    '''
    if ts is None:
        ts = get_ts()
    ret = ''
    if type == 'Y':
        ret = time.strftime('%Y', time.localtime(ts))
    elif type == 'm':
        ret = time.strftime('%Y-%m', time.localtime(ts))
    elif type == 'd':
        ret = time.strftime('%Y-%m-%d', time.localtime(ts))
    elif type == 'H':
        ret = time.strftime('%Y-%m-%d %H-%M', time.localtime(ts))
    elif type == 'M':
        ret = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(ts))
    elif type == 'S':
        ret = time.strftime('%Y-%m-%d %H', time.localtime(ts))
    return ret


# date fomart YY-MM-DD
def date2ts(date):
    return time.mktime(time.strptime(date, '%Y-%m-%d'))


def time2ts(date):
    """
    :param date:
    :return: 时间轴
    """
    return time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S'))


# 计算两天相差的天数
def d_value_day(ts, now_ts=get_ts()):
    d1 = get_day(ts)
    d2 = get_day(now_ts)
    date_list1 = d1.split('-')
    date_list2 = d2.split('-')
    d1 = datetime.datetime(int(date_list1[0]), int(date_list1[1]), int(date_list1[2]))
    d2 = datetime.datetime(int(date_list2[0]), int(date_list2[1]), int(date_list2[2]))
    return (d2 - d1).days


def GenPassword(length=8, chars=string.ascii_letters + string.digits):
    return ''.join([random.choice(chars) for i in range(length)])


def transtime(time):
    return datetime.datetime.strptime(str(time), '%Y%m%d').strftime('%Y-%m-%d')


def get_weekenk_time(ctime, ts):
    '''
    :param ctime:
    :param ts:
    :return: 输出ctime所在周截止到ts 的周末时间
    '''
    saturday_start_stamp, sunday_end_time = get_weekend_full_stamp(ctime)
    if ctime <= saturday_start_stamp:
        if sunday_end_time >= ts > saturday_start_stamp:
            return ts - saturday_start_stamp
        elif ts <= saturday_start_stamp:
            return 0
        else:
            return 86400 * 2
    else:
        if ts <= sunday_end_time:
            return ts - ctime
        else:
            return sunday_end_time - ctime


def get_weekend_full_stamp(ctime):
    '''
    :param ctime: 传入 一个时间轴
    :return:   输出 这个时间轴对应的这个周的周末的 起始时间自 和结束时间轴
    '''
    str = time.strftime("%Y-%m-%d", time.localtime(ctime))
    c_start_stamp = long(time.mktime(time.strptime(str, '%Y-%m-%d')))

    day = time.localtime(ctime).tm_wday
    if day == 5:
        return c_start_stamp, c_start_stamp + 86400 * 2
    elif day == 6:
        return c_start_stamp - 86400, c_start_stamp + 86400
    else:
        saturday_start_stamp = (5 - day) * 86400 + c_start_stamp
        return saturday_start_stamp, saturday_start_stamp + 86400 * 2


def get_month_start_end_ts():
    ts = get_ts()
    month_start_ts = 0
    month_end_ts = 0
    date = get_month(ts)
    month_start_ts = time2ts('{}-01 00:00:01'.format(date))

    date_list = date.split('-')
    if int(date_list[1]) == 12:
        year = int(date_list[0]) + 1
        month_end_ts = time2ts('{}-{}-01 00:00:00'.format(year, 01))
    else:
        month_end_ts = time2ts('{}-{}-01 00:00:00'.format(date_list[0], int(date_list[1]) + 1))

    return month_start_ts, month_end_ts - 1


def analysis_user_year(age_str):
    '''
    从多种时间格式提取年份，判断距今年份差值
    :param age_str:1989/7  1989-07 1989.07 1989年7月 1989 1989年
    :return:{int} 差值
    '''
    year, month = analysis_year_month(age_str)
    year_delay = -1
    if year != 0:
        now_year = datetime.datetime.now().year
        year_delay = now_year - int(year)
    return year_delay


def analysis_year_month(y_m_str):
    '''
    多种时间格式提取年、月, 如果输入为至今则返回当前年月
    :param y_m_str: 1989/7  1989-07 1989.07 1989年7月 1989 1989年 至今
    :return: {int} year,month
    '''
    y_m_str = y_m_str.strip(' ')
    if y_m_str == u'至今':
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
    else:
        if isinstance(y_m_str, str) or isinstance(y_m_str, unicode):
            if len(y_m_str) == 4:
                try:
                    year = int(y_m_str)
                    month = 0
                except  Exception, e:
                    year, month = 0, 0
            else:
                format_data2 = re.compile(u'(\d*)\.(\d*)\.(\d*)')
                year_month = re.findall(format_data2, y_m_str)
                if len(year_month) == 0:
                    format_data2 = re.compile(u'(\d*)/(\d*)/(\d*)')
                    year_month = re.findall(format_data2, y_m_str)
                if len(year_month) == 0:
                    format_data2 = re.compile(u'(\d*)-(\d*)-(\d*)')
                    year_month = re.findall(format_data2, y_m_str)
                if len(year_month) == 0:
                    format_data2 = re.compile(u'(\d*)年(\d*)月(\d*)日')
                    year_month = re.findall(format_data2, y_m_str)
                if len(year_month) == 0:
                    format_data2 = re.compile(u'(\d*)年(\d*)月')
                    year_month = re.findall(format_data2, y_m_str)
                if len(year_month) == 0:
                    format_data2 = re.compile(u'(\d*)-(\d*)')
                    year_month = re.findall(format_data2, y_m_str)
                if len(year_month) == 0:
                    format_data2 = re.compile(u'(\d*)/(\d*)')
                    year_month = re.findall(format_data2, y_m_str)
                if len(year_month) == 0:
                    format_data2 = re.compile(u'(\d*)\.(\d*)')
                    year_month = re.findall(format_data2, y_m_str)
                if len(year_month) == 0:
                    format_data2 = re.compile(u'(\d*)年')
                    try:
                        year_month = re.findall(format_data2, y_m_str)
                        if len(year_month) == 1:
                            year_month = [(year_month[0], 0)]
                    except Exception as e:
                        year, month = 0, 0
                try:
                    year, month = year_month[0][:2] if len(year_month) == 1 else (0, 0)
                    year = int(year) if year != '' else 0
                    month = int(month) if month != '' else 0
                except Exception as e:
                    year, month = 0, 0
        elif type(y_m_str) == type(0):
            year, month = y_m_str, 0
        else:
            year, month = 0, 0
    return year, month


def random_int(min=0, max=10000):
    '''
    获取随机数
    :param min: {int} 最小
    :param max: {int} 最大
    :return: {int} 随机数
    '''
    return random.randint(min, max)


def unquote(str_data):
    return urllib.unquote(str_data)


def file_copy(param=''):
    ret = copy.deepcopy(param)
    return ret


if __name__ == '__main__':
    pass
