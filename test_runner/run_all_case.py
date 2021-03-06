#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: run_all_case.py
# @time: 2020/11/29 4:28 下午

import os
import sys
import shutil
sys.path.append( os.path.join(os.path.dirname(__file__),'..') )
import unittest
from utils import HTMLTestReportCN
from utils.email_utils import EmailUtils
from utils.config_utils import local_config
from nb_log import LogManager

logger = LogManager('P3P4_API_TEST').get_logger_and_add_handlers\
    (is_add_stream_handler=True,log_filename=local_config.LOG_NAME)
current_path = os.path.dirname(__file__)
case_path = os.path.join( current_path,'..','testcases')
result_path = os.path.join( current_path,'..',local_config.REPORT_PATH )

def load_testcase():
    logger.info('加载接口测试用例')
    discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                   pattern='test_api_case.py',
                                                   top_level_dir=case_path)
    all_case_suite = unittest.TestSuite()
    all_case_suite.addTest( discover )
    return all_case_suite

result_dir = HTMLTestReportCN.ReportDirectory(result_path)
result_dir.create_dir('P3P4接口自动化测试报告_')
report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
report_html_obj = open( report_html_path,'wb' )
runner = HTMLTestReportCN.HTMLTestRunner(stream=report_html_obj,
                                         title='P3P4接口自动化测试报告',
                                         description='数据驱动+关键字驱动测试框架学习',
                                         tester='P3P4')
logger.info('接口自动化测试开始执行')
runner.run( load_testcase() )
report_html_obj.close()
# EmailUtils('微信公共号接口测试报告',report_html_path).send_mail()
# os.system('cp -f %s /Users/liuqingjun/software/jenkins/workspace/p3p4_demo_03/接口自动化测试报告.html'
#           %report_html_path)
# os.system('cp -f %s %s/接口自动化测试报告.html'%(report_html_path,sys.argv[1]))
# windows操作系统 可能用 os.sysytem('copy....')不能复制
shutil.copyfile(report_html_path,'%s/接口自动化测试报告.html'%sys.argv[1])
