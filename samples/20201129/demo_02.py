#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_02.py
# @time: 2020/11/29 8:59 上午

import re
str2 = '{"tag":{"id":134,"name":"广东"}}'
v = re.findall( '"id":(.+?),',str2)[0]
print( v )
