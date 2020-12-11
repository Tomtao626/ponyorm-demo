#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: init_table.py 
@time: 2020/12/11
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

from db.db_conf import pony_db
# 生成mapping并建表
pony_db.generate_mapping(create_tables=True)