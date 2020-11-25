#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_01.py
# @time: 2020/11/25 8:19 下午

import json
import requests
import jsonpath

session = requests.session()

get_param_dict={
    "grant_type":"client_credential",
    "appid":"wx55614004f367f8ca",
    "secret":"65515b46dd758dfdb09420bb7db2c67f"
}
response = session.get( url='https://api.weixin.qq.com/cgi-bin/token',
                         params=get_param_dict)
response.encoding = response.apparent_encoding
v = response.json()
v1 = jsonpath.jsonpath( v, '$.access_token' )[0]
print( v1 )
# value = jsonpath.jsonpath(response.json(),requests_info['取值代码'])[0]

v2 = '{"access_token":"..."}'
print( json.loads( v2 ) )
