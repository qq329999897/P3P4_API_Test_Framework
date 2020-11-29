#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_03.py
# @time: 2020/11/29 9:14 上午

import json

str1 = '{"access_token":"39_qHfCmB0GdutZ2MXC0G5IbzrM3WY7ES3JQF_bY04G-ceI-umT7_9E7-m0e3lVx-YFJRcTMnmKga-ijt45IFCrBPeIbbq0PsFphgzjAyaAeYhk8Po13Ix7oQQAi-a85xplVyuERp_rIci3wiP1CRKiAFAIXQ","expires_in":7200}'
#实现一：检查key是否存在
json_obj = json.loads( str1 )
if 'access_token' in json_obj.keys():
    print( 'True' )
else:
    print('Flase')
#实现二：检查多个key是否存在
print( '***************' )
check_keys = ['access_toke','expires_in']
yes_no = []
for check_key in check_keys:
    if check_key in json_obj.keys():
        yes_no.append(True)
    else:
        yes_no.append(False)
if False in yes_no:
    print('False')
