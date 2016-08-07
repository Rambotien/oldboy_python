#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

#print(sys.path)
import os
base_dir =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)

from config import settings
def db_auth(configs):
    if configs.DATABASE["user"]  == 'root' and configs.DATABASE["password"] == '123':
        print("db authentication passed!")
        return True
    else:
        print("db login error...")
def select(table,column):
    if db_auth(settings):
        if table == 'user':
            user_info = {
                "001":['alex',22,'engineer'],
                "002":['longGe',43,'chef'],
                "003":['xiaoYun',23,'13baoan'],
            }
            return user_info

def home():
    print("home fromsql api")