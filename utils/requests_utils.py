#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: requests_utils.py
# @time: 2020/11/18 8:07 下午

import json
import requests
from utils.config_utils import local_config

class RequestsUtils:
    def __init__(self):
        self.hosts = local_config.HOSTS
        self.session = requests.session()
    def __get(self,requests_info):
        url = self.hosts + requests_info['请求地址']
        response = self.session.get( url = url,
                                     params = json.loads(requests_info['请求参数(get)']),
                                     headers = requests_info['请求头部信息'])
        response.encoding = response.apparent_encoding #保证不乱码
        result = {
            'code':0,
            'response_code':response.status_code,
            'response_reason':response.reason,
            'response_headers':response.headers,
            'response_body':response.text
        }
        return result

    def __post(self,requests_info):
        url = self.hosts + requests_info['请求地址']
        response = self.session.post(url=url,
                                     headers=requests_info['请求头部信息'],
                                     params=json.loads(requests_info['请求参数(get)']),
                                     json = json.loads(requests_info['请求参数(post)'])
                                    )
        response.encoding = response.apparent_encoding
        result = {
            'code':0,
            'response_code':response.status_code,
            'response_reason':response.reason,
            'response_headers':response.headers,
            'response_body':response.text
        }
        return result

    def request(self,step_info):
        request_type = step_info['请求方式']
        if request_type == "get":
            result = self.__get(step_info)
        elif request_type == "post":
            result = self.__post(step_info)
        else:
            result = {'code':1,'result':'请求方式不支持'}
        return result

    def request_by_step(self,test_steps):
        for test_step in test_steps:
            result = self.request(test_step)
            if result['code'] != 0:
                break
        return result




if __name__=='__main__':
    # req_post_dict = {'测试用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_03', '接口名称': '删除标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":"39_ZlzNDPma7qLWpLJ4K0ir_cSahJ_fg9aevBpGvqRp9VNjqRE6hSkBOSUFla-mFjSGKyF-YFx28sM4Ch1rJISPGVSTahZ8l_xQ9M7CnAFoqUfibusAdeOI4lHEIzB6zhXJQHN5b9as9zhcGtSbBYKeAGAEBN"}', '请求参数(post)': '{   "tag":{        "id" : 456   } }'}
    # req_dict = {'测试用例编号': 'api_case_01', '测试用例名称': '获取access_token接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '请求参数(post)': ''}
    step_list = [{'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '请求参数(post)': ''}, {'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":"39_Bm5UI-zvWkokwnl6d3zCW30hk3sVHSv6sh6cHN3dbgnwUdfmhM-EFZ3OIrTechkzaRt9Iae3yX_MF7_h7bobNybvkoAC1CM2pAfGfNqSegXsPbjyJzkgSHtBV1OezPwEvFn60jS3__w5BdzVMRHcAHAYDT"}', '请求参数(post)': '{   "tag" : {     "name" : "广东" } } '}]
    requestsUtils = RequestsUtils()
    requestsUtils.request_by_step( step_list )
    # print( v )




