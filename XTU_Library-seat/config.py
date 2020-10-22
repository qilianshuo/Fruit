#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 7:42
# @Author  : Qi
# @Email   : 2087989820@qq.com
# @File    : config.py
# @Software: PyCharm


"""!!! login_link很重要!!! 很重要!!! 自己在手机APP湘大校园抓包"""
login_link = ''
DATA_URL = 'http://wechat.v2.traceint.com/data/'
STATIC_URL = 'http://static.wechat.v2.traceint.com/static/'
BASE_URL = 'http://wechat.v2.traceint.com'
SELECT_URL = 'http://wechat.v2.traceint.com/index.php/reserve/get/libid='
ROOM_URL = 'http://wechat.v2.traceint.com/index.php/reserve/index.html'
# seat_list_url = 'http://wechat.v2.traceint.com/index.php/reserve/mylist.html'
seat_list_url = 'http://wechat.v2.traceint.com/index.php/reserve/index.html'

headers = {
    'Host': 'wechat.v2.traceint.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

libid = 116992
seat_coordinate = '17,15'
