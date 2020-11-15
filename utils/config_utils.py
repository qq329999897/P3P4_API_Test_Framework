#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: config_utils.py
# @time: 2020/11/15 11:36 上午

import os
import configparser

current_path = os.path.dirname(__file__)
config_file_path = os.path.join( current_path,'..','conf','localconfig.ini' )

class ConfigUtils:
    def __init__(self,cfg_path=config_file_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(cfg_path)
    @property
    def HOSTS(self):
        hosts_value = self.cfg.get('default','hosts')
        return hosts_value

local_config = ConfigUtils()

if __name__=='__main__':
    print( local_config.HOSTS )