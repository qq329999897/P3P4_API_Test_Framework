#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: excel_oper_01.py
# @time: 2020/11/15 11:50 上午

import xlrd3
workbook = xlrd3.open_workbook('test_data.xlsx')
sheet = workbook.sheet_by_name('Sheet1')
print( sheet.cell_value(0,3) )
print( sheet.cell_value(1,0) )
print( sheet.cell_value(2,0) )
print( sheet.merged_cells ) # 包含四个元素（起始行，结束行，起始列，结束列）

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

#  for 循环支持同时使用元组中的多个变量做成参数
for  (min_row,max_row,min_col,max_col)  in [(1, 5, 0, 1)]:
    print( min_row,min_col,max_row,max_col )
# 解决合并单元格值为空的问题
row_index = 1 ; col_index = 2
for (min_row,max_row,min_col,max_col) in sheet.merged_cells:
    if row_index >= min_row and row_index < max_row:
        if col_index >= min_col and col_index < max_col:
            cell_value = sheet.cell_value(min_row,min_col) # 合并单元格的值等于合并第一个单元格的值
        else:
            cell_value = sheet.cell_value(row_index,col_index)
    else:
        cell_value = sheet.cell_value(row_index, col_index)
print( cell_value )
# 做成方法
def get_cell_merged_value(row_index,col_index):
    for (min_row, max_row, min_col, max_col) in sheet.merged_cells:
        if row_index >= min_row and row_index < max_row:
            if col_index >= min_col and col_index < max_col:
                cell_value = sheet.cell_value(min_row, min_col)  # 合并单元格的值等于合并第一个单元格的值
            else:
                cell_value = sheet.cell_value(row_index, col_index)
        else:
            cell_value = sheet.cell_value(row_index, col_index)
    return cell_value