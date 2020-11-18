#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: requests_demo_01.py
# @time: 2020/11/18 8:08 下午

import requests

session = requests.session()

get_param_dict={
    "grant_type":"client_credential",
    "appid":"wx55614004f367f8ca",
    "secret":"65515b46dd758dfdb09420bb7db2c67f"
}

response = session.get( url='https://api.weixin.qq.com/cgi-bin/token',
                         params=get_param_dict)
print( response.content.decode('utf-8') )


