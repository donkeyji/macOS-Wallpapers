#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-15
# @Author  : yiming (kevinjobs@qq.com)
# @Link    : kevinjobs.github.io
# @Version : 1.0

import os
import time
import datetime
import requests
from bs4 import BeautifulSoup
import lxml
import json

TOKEN = '' # 请填入自己的 Unsplash API 的 token，在 https://unsplash.com/developer 申请
URL = 'https://api.unsplash.com/photos/random?client_id=' + TOKEN
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

# socks 代理，视你的网络情况是否启用代理，
# 如要代理,请安装 pip install "requests[socks]"
PROXIES = {'http': 'socks5://127.0.0.1:1086', 'https': 'socks5://127.0.0.1:1086'} 


def crawl():
    '''
    :return: 返回供 shell 脚本读取的文本
    '''
    tmp = _get_page(URL)
    html = tmp.text
    soup = _get_soup(html)
    json_cont = soup.get_text()
    adict = _parse_json(json_cont)
    pic_id = adict['id']
    download_links = adict['links']['download']
    source_url = adict['links']['html']
    _save_pic(pic_id, download_links)
    _write_info(pic_id, source_url)
    print(pic_id)

def _get_page(url):

    r = requests.get(url, headers=HEADERS, proxies=PROXIES) # 在这里启用代理
    return r

def _get_soup(html):

    soup = BeautifulSoup(html, 'lxml')
    return soup

def _parse_json(json_cont):

    adict = json.loads(json_cont)
    return adict

def _save_pic(title, url):

    r = _get_page(url)
    _make_path('images')
    if r:
        with open(r'images/%s.jpg' %title, 'wb') as pic:
            for chunk in r.iter_content(chunk_size=1024):
                pic.write(chunk) # 写入图片
    else:
        pass

def _write_info(title, source_url):

    date = datetime.datetime.now()
    if title:
        # 写入日志
        with open(r'images/下载日志.log', 'a+') as fp:
            fp.write('DATE:%s - DESCRIPTION: %s, URL: %s\n' %(date, title, source_url))
    else:
        pass

def _make_path(path):

    # 判断文件夹是否存在
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)

if __name__ == '__main__':
    crawl()
