#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_02.py
# @time: 2020/11/25 8:46 下午

import re
import ast
import json

str1 = '{"access_token":${token}}'
variables_list = re.findall('\\${\w+}',str1)
print( variables_list )
dict1 = {'token': 'AFABMG'}
# str1 = str1.replace(variables_list[0],'"%s"'%'AFABMG')
# print( dict1[variables_list[0][2:-1]] )
str1 = str1.replace(variables_list[0],'"%s"'%dict1[ variables_list[0][2:-1] ])
print( str1 )

#成果：{"access_token":"AFABMG"}  考虑：多个变量怎么办？ 不需要替换的情况怎么办？
str2 = 'a   ${a}    a'#'{"name":${n},"age":${a}}'
dict2 = {'n': 'xiaoming','a':18}
variables_list1 = re.findall('\\${\w+}',str2)
print( variables_list1 )
for v in variables_list1:
    str2 = str2.replace( v,'"%s"'%dict2[v[2:-1]] )
print( str2 )

str3 = "{'name':'xiaoming'}"
str4 = '{"name":"xiaoming"}'
print( json.loads(str4) )
print( ast.literal_eval( str3 ) )
