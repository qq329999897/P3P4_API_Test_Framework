#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: data_convert_01.py
# @time: 2020/11/15 4:10 下午

a_dict = {'小红':[{'book1':'朝花夕拾'},{'book2':'红楼梦'}],
          '小黑':[{'book1':'呐喊'},{'book2':'红楼梦'}]}
data_list = []
for key,value in a_dict.items():
    b_dict = {}
    b_dict['name'] = key
    b_dict['books'] = value
    data_list.append(b_dict)
print( data_list )


