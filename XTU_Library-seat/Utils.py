#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 15:48
# @Author  : Qi
# @Email   : 2087989820@qq.com
# @File    : Utils.py
# @Software: PyCharm
import re
import time
import execjs
import requests


def insert_str(str_1, str_2, index):
    str_list = list(str_1)
    str_list.insert(index, str_2)
    return ''.join(str_list)


def get_seat_key(js_url):
    jscode = requests.get(js_url).content.decode('GBK')
    key = re.findall(r'AJAX_URL\+"libid="\+[a-zA-Z]\+"&"\+(.*?)\+"="', jscode)[0]
    jscode = re.sub(r'T.ajax_get\(.*\)', '', jscode)
    final_code = insert_str(jscode, 'return ' + key, -2)
    ctx = execjs.compile(final_code)
    return ctx.call('reserve_seat')

def log_print(str):
    print(time.strftime("[%m-%d %H:%M:%S] ", time.localtime()), end='')
    print(str)
