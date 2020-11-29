#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_05.py
# @time: 2020/11/29 10:40 上午

class Demo5:
    def __init__(self):
        self.function = {
            'json_key': self.key_check,
            'json_key_value': self.key_value_check
        }
    def key_check(self):
        print( 'key_check.....' )
    def key_value_check(self):
        print( 'key_value_check.....' )

    def run_check(self,check_type):
        self.function[check_type]()

if __name__=='__main__':
    demo5 = Demo5()
    demo5.run_check( 'json_key_value' )

