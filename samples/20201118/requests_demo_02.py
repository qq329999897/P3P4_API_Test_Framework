#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: requests_demo_01.py
# @time: 2020/11/18 8:08 下午

import requests

session = requests.session()

response = session.get(url='http://www.hnxmxit.com/')
print( response.headers )  # 'charset=utf-8' 默认编码格式改为 ISO-8859-1
response.encoding = response.apparent_encoding # 网页的内容中分析网页的编码方式
print( response.text )


