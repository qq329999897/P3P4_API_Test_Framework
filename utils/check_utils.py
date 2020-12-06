#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: check_utils.py
# @time: 2020/11/29 9:31 上午

import requests
import json
import re
from nb_log import LogManager
from utils.config_utils import local_config

logger = LogManager('P3P4_API_TEST').get_logger_and_add_handlers(is_add_stream_handler=True,
                                                        log_filename=local_config.LOG_NAME)

class CheckUtils:
    def __init__(self,response_data):
        self.response_data = response_data
        self.check_rules = {
            'none': self.none_check,
            'json_key': self.body_key_check,
            'json_key_value': self.body_key_value_check,
            'body_regexp': self.regexp_check,
            'header_key': self.header_key_check,
            'header_key_value': self.header_key_value_check,
            'response_code': self.response_code_check
        }
        self.pass_result = {
            'code':0,
            'response_code':self.response_data.status_code,
            'response_reason':self.response_data.reason,
            'response_headers':self.response_data.headers,
            'response_body':self.response_data.text,
            'response_url':self.response_data.url,
            'message':'',
            'check_result': True
        }
        self.fail_result = {
            'code':1,
            'response_code':self.response_data.status_code,
            'response_reason':self.response_data.reason,
            'response_headers':self.response_data.headers,
            'response_body':self.response_data.text,
            'response_url':self.response_data.url,
            'message': '',
            'check_result': False
        }

    def none_check(self):
        logger.info( '断言类型为无或期望结果无数据，检测通过' )
        return self.pass_result

    def __key_check(self,actual_result,check_data):
        key_list = check_data.split(',')
        tmp_result = []
        for key in key_list:
            if key in actual_result.keys():
                tmp_result.append( self.pass_result )
            else:
                tmp_result.append( self.fail_result )
        if self.fail_result in tmp_result:
            logger.info('测试实际结果: %s 测试期望结果：%s 不一致，检测失败'%(json.dumps(actual_result,ensure_ascii=False),check_data))
            return self.fail_result
        else:
            logger.info('测试实际结果: %s 测试期望结果：%s 一致，检测通过'%(json.dumps(actual_result,ensure_ascii=False),check_data))
            return self.pass_result

    def header_key_check(self,check_data):
        return self.__key_check(self.response_data.headers,check_data)

    def body_key_check(self,check_data):
        return self.__key_check(self.response_data.json(),check_data)

    def __key_value_check(self,actual_result,check_data):
        key_value_dict = json.loads( check_data )
        tmp_result = []
        for key_value in key_value_dict.items():
            if key_value in actual_result.items():
                tmp_result.append( self.pass_result )
            else:
                tmp_result.append( self.fail_result )
        if self.fail_result in tmp_result:
            logger.info('测试实际结果: %s 测试期望结果：%s 不一致，检测失败'%(json.dumps(actual_result,ensure_ascii=False),check_data))
            return self.fail_result
        else:
            logger.info('测试实际结果: %s 测试期望结果：%s 一致，检测通过' % (json.dumps(actual_result,ensure_ascii=False), check_data))
            return self.pass_result

    def header_key_value_check(self,check_data):
        return self.__key_value_check(self.response_data.headers,check_data)

    def body_key_value_check(self,check_data):
        return self.__key_value_check(self.response_data.json(),check_data)

    def response_code_check(self,check_data):
        if self.response_data.status_code == int(check_data):
            logger.info('实际响应状态码：%s 期望结果：%s 一致，检测通过' %(str(self.response_data.status_code),check_data))
            return self.pass_result
        else:
            logger.info('实际响应状态码：%s 期望结果：%s 不一致，检测失败' %(str(self.response_data.status_code),check_data))
            return self.fail_result

    def regexp_check(self,check_data):
        tmp_result = re.findall(check_data,self.response_data.text)
        if tmp_result:
            logger.info('期望结果正则表达式：%s 能在响应正文进行匹配，检测通过' % check_data)
            return self.pass_result
        else:
            logger.info('期望结果正则表达式：%s 不能在响应正文进行匹配，检测失败' % check_data)
            return self.fail_result

    def run_check(self,check_type,check_data):
        logger.info('根据 %s 进行断言，检查是否满足期望结果：%s'%(check_type,check_data))
        if check_type=='none' or check_data == '':
            return self.check_rules['none']()
        else:
            return self.check_rules[check_type](check_data)





if __name__=='__main__':
    session = requests.session()
    get_param_dict = {
        "grant_type": "client_credential",
        "appid": "wx55614004f367f8ca",
        "secret": "65515b46dd758dfdb09420bb7db2c67f"
    }
    response = session.get(url='https://api.weixin.qq.com/cgi-bin/token',
                           params=get_param_dict)
    response.encoding = response.apparent_encoding
    checkUtils = CheckUtils(response)
    print( response.headers )
    # print( checkUtils.key_check('access_token,expires_in') )
    # print( checkUtils.key_value_check('{"expires_in":7200}') )
    print( checkUtils.run_check('json_key','access_token,expires_in') )
    print( checkUtils.run_check('json_key_value','{"expires_in":7200}') )
    print( checkUtils.run_check('body_regexp','"access_token":"(.+?)sss"') )
    print( checkUtils.run_check('header_key','Connection,Content-Length') )
    print( checkUtils.run_check('header_key_value','{"Connection":"keep-alive"}') )



