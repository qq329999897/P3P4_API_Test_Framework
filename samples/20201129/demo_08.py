#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_08.py
# @time: 2020/11/29 3:01 下午

import paramunittest
import unittest

@paramunittest.parametrized(
    (50,20),
    (30,40),
    (100,20)
)
class ApiTestDemo(paramunittest.ParametrizedTestCase):  #unittest.TestCase
    def setParameters(self, numa,numb):
        self.a = numa
        self.b = numb
    def test_add_case(self):
        print( '%d+%d?=%d'%(self.a,self.b,30) )
        self.assertEqual( self.a + self.b,30 )

if __name__=='__main__':
    unittest.main(verbosity=2)
