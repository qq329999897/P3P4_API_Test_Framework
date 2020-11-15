#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: excel_oper.py
# @time: 2020/11/15 11:50 上午

import xlrd3

workbook = xlrd3.open_workbook('test_data.xlsx')
sheet = workbook.sheet_by_name('Sheet1')
print( sheet.cell_value(0,3) )
print( sheet.cell_value(1,0) )
print( sheet.cell_value(2,0) )
print( sheet.merged_cells ) # 数组包含四个元素（起始行，结束行，起始列，结束列）

# 给出一个行列，判断一个单元格是否是合并过的
x = 2
y = 0
if x>=1 and x<5:
    if y>=0 and y<1:
        print( '合并单元格' )
    else:
        print('不是合并单元格')
else:
    print('不是合并单元格')
