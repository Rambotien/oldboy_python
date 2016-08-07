#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle
import json

def login():
    print("hello")

f = open("user_acc.txt","wb")

info={
    "alex":"123",
    "jack":'4444',
    "func":login
}

pickle.dump(info,f)
#print(pickle.dumps(info))
#f.write(pickle.dumps(info))
f.close()