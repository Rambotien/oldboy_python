#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle,json
def  login():
    print("hahaha")
f =open("user_acc.txt","rb")

#data_from_atm =pickle.loads(f.read())
data_from_atm= pickle.load(f)

data_from_atm['func']()
print(data_from_atm)