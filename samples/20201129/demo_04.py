#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_04.py
# @time: 2020/11/29 9:47 上午

import json

json_obj = {"access_token":"39_qHfCmB0GdutZ2MXC0G5IbzrM3WY7ES3JQF_bY04G-ceI-umT7_9E7-m0e3lVx-YFJRcTMnmKga-ijt45IFCrBPeIbbq0PsFphgzjAyaAeYhk8Po13Ix7oQQAi-a85xplVyuERp_rIci3wiP1CRKiAFAIXQ","expires_in":7200}
except_str = '{"expires_in":7200,"key":18}'
except_dict = json.loads(except_str)
print( except_dict.items() )
print( json_obj.items() )
# 方式一：
if list(except_dict.items())[0] in list(json_obj.items()):
    print( 'true' )

# 方式二：考虑多项
yes_no = []
for except_item in except_dict.items():
    if except_item in json_obj.items():
        yes_no.append( True )
    else:
        yes_no.append( False )
if False in yes_no:
    print( 'False' )
else:
    print( 'true' )

