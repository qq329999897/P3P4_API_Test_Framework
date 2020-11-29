#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_06.py
# @time: 2020/11/29 11:44 上午

str1 = {"errcode":45157,"errmsg":"invalid tag name hint: [ufofmzNre-xPogda] rid: 5fc31853-65c5781c-589a24b3"}
check_data = "tag"

def key_check(check_data):
    key_list = check_data.split(',')
    tmp_result = []
    for key in key_list:
        if key in str1.keys():
            tmp_result.append(True)
        else:
            tmp_result.append(False)
    if False in tmp_result:
        return False
    else:
        return True

print( key_check(check_data) )
