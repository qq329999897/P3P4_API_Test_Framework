#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: data_convert_01.py
# @time: 2020/11/15 4:10 下午

a = {'one':1,'two':2,'three':3}
a.setdefault('four',4) #设置默认值  key不存在新增键值对
print( a )
print( a.setdefault('two',10) ) # key存在 不会修改内容
print( a )

data_list = [{'事件': '学习python编程', '步骤序号': 'step_01', '步骤操作': '购买微课', '完成情况': 100.0}, {'事件': '学习python编程', '步骤序号': 'step_02', '步骤操作': '搭建环境', '完成情况': 100.0}, {'事件': '学习python编程', '步骤序号': 'step_03', '步骤操作': '做笔记', '完成情况': 90.0}, {'事件': '学习python编程', '步骤序号': 'step_04', '步骤操作': '应用', '完成情况': 80.0}, {'事件': '学习java编程', '步骤序号': 'step_01', '步骤操作': '购买微课', '完成情况': 100.0}, {'事件': '学习java编程', '步骤序号': 'step_02', '步骤操作': '搭建环境', '完成情况': 100.0}, {'事件': '学习java编程', '步骤序号': 'step_03', '步骤操作': '做笔记', '完成情况': 90.0}, {'事件': '学习java编程', '步骤序号': 'step_04', '步骤操作': '应用', '完成情况': 80.0}]
data_dict = {}
for d in data_list:
    data_dict.setdefault(d['事件'],[]).append( d )  # python 精髓代码
print( data_dict )

