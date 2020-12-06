#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: json_demo_03.py
# @time: 2020/12/6 2:39 下午

import json

str1 = '{"tag":{"name":"邵阳"}}'
json_obj = json.loads(str1)
str2 = json.dumps( json_obj,ensure_ascii=False )
print( str2 )