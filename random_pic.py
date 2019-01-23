#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-15
# @Update  : 2019-01-23
# @Author  : 
# @Link    : 
# @Version : 1.0

import os
import datetime
import requests
import json

TOKEN = '' # 填入你自己的 Access Key
URL = 'https://api.unsplash.com/photos/random?client_id=' + TOKEN
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

PROXIES = {'http': 'socks5://127.0.0.1:1086', 'https': 'socks5://127.0.0.1:1086'}
# 为了使用代理，你需要安装 pip3 install requests['socks']

def crawl(url):
    '''
    :return: return the id for the sh script
    '''
    # get the json content from unsplash API
    json_cont = _get_response(url).text
    # json to python dict
    adict = json.loads(json_cont)
    # title is the description of the picture
    title = adict['description']
    # extract the link
    download_links = adict['links']['download']
    # the raw page
    source_url = adict['links']['html']
    # to save image
    _save_pic(title, download_links)
    # log
    _write_info(title, source_url)
    # print to the shell script
    # the shell script catch a title from this
    print(title)

def _get_response(url):

    r = requests.get(url, headers=HEADERS, proxies=PROXIES) # use proxy if neccessary
    return r

def _save_pic(title, url):

    r = _get_response(url) # get the response
    _make_path('images')
    if r:
        with open(r'images/%s.jpg' %title, 'wb') as pic:
            for chunk in r.iter_content(chunk_size=1024):
                pic.write(chunk) # write to the image file
    else:
        pass

def _write_info(title, source_url):

    date = datetime.datetime.now()
    if title:
        with open(r'images/下载日志.log', 'a+') as fp:
            fp.write('DATE: {}, URL: {}, DESCRIPTION: {}\n'.format(date, source_url, title))
    else:
        pass

def _make_path(path):

    # judge the path's existence
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)

if __name__ == '__main__':
    crawl(URL)
