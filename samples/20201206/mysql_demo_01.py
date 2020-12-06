#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: mysql_demo_01.py
# @time: 2020/12/6 10:29 上午

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='interface_test_db',
    charset='utf8'
)

cursor = conn.cursor( cursor=pymysql.cursors.DictCursor )

sql_str = 'select * from case_info;'
cursor.execute( sql_str )
print( cursor.fetchall() )

cursor.close()
conn.close()