#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: testcase_data_utils.py
# @time: 2020/11/15 4:48 下午

import os
from utils.excel_utils import ExcelUtils

excel_file_path = os.path.join( os.path.dirname(__file__),'..','data','testcase_infos.xlsx')
excel_sheet_name = 'Sheet1'

class TestcaseDataUtils:
    def __init__(self):
        self.excel_data = ExcelUtils(excel_file_path=excel_file_path,sheet_name=excel_sheet_name)


    def convert_testcase_data_to_dict(self):
        ''' 把excel的所有原始数据转换成符合框架需要的测试用例业务数据 '''
        testcase_dict = {}
        for row_data in self.excel_data.get_all_data():
            testcase_dict.setdefault(row_data['测试用例编号'],[]).append(row_data)
        return testcase_dict

    def convert_testcase_data_to_list(self):
        ''' 把convert_testcase_data_to_dict产生的数据转换成列表并在每个元素中增加key '''
        all_casedata_list = []
        for key,value in self.convert_testcase_data_to_dict().items():
            case_info_dict = {}
            case_info_dict['case_id'] = key
            case_info_dict['case_step'] = value
            all_casedata_list.append( case_info_dict )
        return all_casedata_list

if __name__=='__main__':
    testcaseDataUtils = TestcaseDataUtils()
    test_case_lists = testcaseDataUtils.convert_testcase_data_to_list()
    # for testcase in test_case_dicts['api_case_01']:
    #     print( testcase )
    for t in test_case_lists:
        print( t )

