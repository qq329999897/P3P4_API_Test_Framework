#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_01.py
# @time: 2020/12/2 9:20 下午

from nb_log import LogManager

logger = LogManager('newdream').get_logger_and_add_handlers(is_add_stream_handler=True,
                                                          log_filename='newdream.log')

logger.info('蓝色')