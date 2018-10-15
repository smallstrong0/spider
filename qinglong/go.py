#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 01:07
# @Author  : SmallStrong
# @Des     :
# @File    : go.py
# @Software: PyCharm

from selenium import webdriver
import config
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('lang=zh_CN.UTF-8')


# chromeOptions.add_argument(
#     'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, '
#     'like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')


# chromeOptions.add_argument('--proxy-server=http://ip:port')


def go():
    driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH, chrome_options=chromeOptions)
    base_url = config.HOST
    tags = ['Chrome']
    for tag in tags:
        driver.get(base_url + tag)
        # for i in range(1, 10):
        #     js = "var q=document.documentElement.scrollTop=" + str(500 * i)  # 谷歌 和 火狐
        #     driver.execute_script(js)
        #     time.sleep(3)
        ul = driver.find_element_by_xpath('//*[@id="juejin"]/div[2]/main/div/div[2]/ul')
        print(len(ul))

        lis = ul.find_elements_by_xpath('li')
        print len(lis)  # 有多少个li
        resutl_dic = {}
        for i in lis:
            pass

    driver.quit()


if __name__ == '__main__':
    go()
