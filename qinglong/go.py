#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 01:07
# @Author  : SmallStrong
# @Des     : 
# @File    : go.py
# @Software: PyCharm

from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()


def go():
    path = "./driver/chromedriver"  # chromedriver完整路径，path是重点
    driver = webdriver.Chrome(path)
    chromeOptions.add_argument('--proxy-server=http://ip:port')
    base_url = 'https://www.baidu.com'
    driver.get(base_url)
    driver.get_screenshot_as_file('./a.png')
    driver.implicitly_wait(90)


if __name__ == '__main__':
    go()
