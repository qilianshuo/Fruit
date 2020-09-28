#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/12 19:48
# @Author  : Qi
# @Email   : 2087989820@qq.com
# @File    : Utils.py
# @Software: PyCharm
import re
import config
import Utils
# import json
import time
import requests
from Utils import log_print
# from bs4 import BeautifulSoup


class Libary:
    def __init__(self):
        self.has_select = 0
        self.session = requests.session()
        self.vacant_room = dict()
        self.vacant_seat = dict()

    def login(self):
        resp = self.session.get(url=config.login_link, headers=config.headers)
        resp.encoding = resp.apparent_encoding
        log_print('登录成功')
        return True

    def find_room(self):
        """
        查找有空余座位的房间
        :return: True || False
        """
        resp = self.session.get(config.ROOM_URL, headers=config.headers)
        resp.encoding = resp.apparent_encoding
        room_list = re.findall(r'<div class="list-group".*?>([\s\S]*?)</div>', resp.text)
        # 如果没找到房间列表直接返回False
        if room_list is None:
            log_print('re查找错误,未匹配到房间列表')
            return False
        pattern = re.compile(r'<a href=".*?" data-url="(.*?)".*?><.*?>(.*?)<.*?>(.*?)<.*?>')
        room_list = pattern.findall(room_list[0].replace('\t', '').replace('\n', ''))
        for room in room_list:
            if int(room[2].split('/')[0]):
                self.vacant_room[room[1]] = config.BASE_URL + room[0]
        if self.vacant_room is None:
            log_print('无空闲房间')
            return False
        else:
            log_print('查找空房间成功!')
            return True

    def find_seat(self):
        log_print('当前选定房间: %s' % list(self.vacant_room.keys())[0])
        resp = self.session.get(url=list(self.vacant_room.values())[0], headers=config.headers)
        resp.encoding = resp.apparent_encoding
        pattern = re.compile(r'<div class="grid_cell {2}grid_1" data-key="(.*?)".*?><em>(\d+)</em></div>')
        seat_list = pattern.findall(resp.text.replace('\n', ''))
        if seat_list:
            for seat in seat_list:
                self.vacant_seat[seat[1]] = seat[0]
            log_print('查找空座成功')
            return True
        else:
            log_print('座位被抢光了!!')
            return False

    def select_seat(self):
        log_print('当前选定座位：%s号' % list(self.vacant_seat.keys())[0])
        resp = self.session.get(list(self.vacant_room.values())[0], headers=config.headers)
        resp.encoding = resp.apparent_encoding
        js_url = re.findall(r'<script src="(.*?)">', resp.text)[1]
        key = Utils.get_seat_key(js_url)
        libid = re.findall(r'libid=(.*?).html', list(self.vacant_room.values())[0])[0]
        select_url = config.SELECT_URL+'%s&%s=%s&yzm=' % (libid, key, list(self.vacant_seat.values())[0])
        result = self.session.get(url=select_url, headers=config.headers).json()
        print(result)
        if result['code'] == 0:
            return True
        else:
            return False

    def refresh_seat(self):
        while self.login() and self.find_room() and self.find_seat() and self.select_seat() is not True:
            time.sleep(1)


if __name__ == "__main__":
    Libary_Seat = Libary()
    Libary_Seat.refresh_seat()
