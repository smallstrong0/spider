#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 23:15
# @Author  : SmallStrong
# @Des     : 默认在output目录下,输出本地文件
# @File    : export_to_local.py
# @Software: PyCharm

import ss.common.func as func
import xlwt
import os


def write_as_py(file_name, data, data_name='default', path='{}/output/'.format(os.getcwd())):
    """
    输出py文件
    :param file_name: py文件名称
    :param data: 要输出的内容（列表 or 字典）
    :param data_name:
    :param path:
    :return:
    """
    f = open("{}{}.py".format(path, file_name), 'w+')
    print >> f, '# !/bin/python'
    print >> f, '# -*- coding: utf8 -*-'
    print >> f, '{} = {}'.format(data_name, func.sort_serialize(data))


def write_to_xls(result_list=None, columns_name_list=None, dic_key_list=None,
                 path='{}/output/'.format(os.getcwd()), file_name='default', sheet_name='默认输出'):
    """
    数据写入Excel
    注意的是columns_name_list与dic_key_list列表的元素位置要一一对应，切记！！！
    :param result_list: 写入的数据 list中是字典
    :param columns_name_list:  第一行属性命名
    :param dic_key_list: list中是字典的key的集合
    :param path: 文件路径
    :param file_name: 文件名
    :param sheet_name: Excel sheet 名称
    :return:
    """
    if not result_list or not columns_name_list or not dic_key_list:
        raise Exception("数据结构传入不符")

    wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = wbk.add_sheet('{}'.format(sheet_name), cell_overwrite_ok=True)

    alignment = xlwt.Alignment()  # Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
    style = xlwt.XFStyle()  # Create Style
    style.alignment = alignment  # Add Alignment to Style

    for c in xrange(len(columns_name_list)):
        sheet.write(0, c, '  {} '.format(columns_name_list[c]), style)

    for i in xrange(len(result_list)):
        for c in xrange(len(dic_key_list)):
            sheet.write(i + 1, c, result_list[i].get(dic_key_list[c], ''), style)
    wbk.save('{}{}.xls'.format(path, file_name))


def write_as_txt(file_name, data, path='{}/output/'.format(os.getcwd())):
    """
    数据写入txt
    :param file_name: 文件名
    :param data: 写入数据
    :param path: 文件路径 默认output目录下
    :return:
    """
    f = file("{}{}.txt".format(path, file_name), "a+")  # 以追加的方式
    f.write(data)
    f.write("\n")  # 写完通过\n进行换行


def test():
    # write_as_py('default_py', {'a': 1})
    # write_to_xls([{'a': 1, 'b': '222'}], ['测试1', '测试2'], ['a', 'b'])
    # write_as_txt('default_txt', data=func.sort_serialize({'1': 11, '2': 22}))
    pass


if __name__ == '__main__':
    test()
