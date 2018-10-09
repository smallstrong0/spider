#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 23:09
# @Author  : SmallStrong
# @Des     : 
# @File    : xcf_parser.py
# @Software: PyCharm

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
import xuanwu.pipeline.export_to_output as export_data
import xuanwu.pipeline.export_to_redis as export_redis
from lxml import etree

redis_cli = export_redis.cli()


def get_category_dic(content):
    result_dic = {}
    result_status = {}
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all("a")
    for link in links:
        if 'category' in link.attrs.get('href', '') and link.string and link.string not in ['查看全部分类', '菜谱分类']:
            result_dic[link.attrs.get('href', '')] = link.string
            result_status[link.attrs.get('href', '')] = 0
    export_data.write('category_dic', 'category_dic', result_dic)
    if result_status:
        redis_cli.hmset('category_dic', result_status)
    return result_dic


def get_recipe_list(category_list_content):
    recipe_dic = {}
    soup = BeautifulSoup(category_list_content, 'html.parser')
    links = soup.find_all("a")
    for link in links:
        if '/recipe/' in link.attrs.get('href', ''):
            recipe_dic[link.attrs.get('href', '')] = 0
    if recipe_dic:
        redis_cli.hmset('recipe_dic', recipe_dic)
    return recipe_dic


def get_content(recipe_content):
    """
    //*[@id="site-body"]/div
    //*[@id="site-body"]/div/div[1]
    //*[@id="site-body"]/div/div[2]
    :param recipe_content:
    :return:
    """
    content_dic = {}
    error = None

    html = etree.HTML(recipe_content)
    dish_img_list = html.xpath('//*[@id="site-body"]/div/div[1]/img/@data-src')
    if len(dish_img_list) > 0:
        content_dic['dish_img'] = dish_img_list[0]

    dish_name_list = html.xpath('//*[@id="name"]/h1/text()')
    if len(dish_name_list) > 0:
        content_dic['dish_name'] = dish_name_list[0]

    desc_list = html.xpath('//*[@id="description"]/p/text()')
    if len(desc_list) > 0:
        content_dic['desc'] = desc_list[0]

    author_list = html.xpath('//*[@id="site-body"]/div/div[2]/section[2]/div/a/span/text()')
    if len(author_list) > 0:
        content_dic['author'] = author_list[0]

    author_logo_list = html.xpath('//*[@id="site-body"]/div/div[2]/section[2]/a/img/@data-src')
    if len(author_logo_list) > 0:
        content_dic['author_logo'] = author_logo_list[0]

    tips_list = html.xpath('//*[@id="tips"]/p/text()')
    if len(tips_list) > 0:
        content_dic['tips'] = tips_list[0]

    materials_list = html.xpath('//*[@id="ings"]/ul/li/a/span/text()')
    if len(materials_list) > 0:
        content_dic['materials'] = materials_list

    step_text_list = html.xpath('//*[@id="steps"]/ul/li/div/p/text()')
    if len(step_text_list) > 0:
        content_dic['steps_texts'] = step_text_list

    step_url_list = html.xpath('//*[@id="steps"]/ul/li/div/div/div/a/img/@data-src')
    if len(step_url_list) > 0:
        content_dic['step_urls'] = step_url_list

    if len(content_dic) != 9 or len(step_text_list) != len(step_url_list) or len(materials_list) % 2 != 0:
        return content_dic, '数据格式有出入'
    return content_dic, error
