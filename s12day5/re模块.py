#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
'''
re.match("[0-9]")
re.match("[a-zA-Z0-9@._]")
re.match("[0123456789]")
'''
string = "592.168.2.23333"
#m =re.match("([0-9]{3}\.){3}",string)
m =re.match("([0-9]{1,3}\.){3}\d{1,3}",string)
print(m.group())

string2 = "alex \njack\nrain\nli"
#string2 = "ALEX"
m = re.search("[a-z]", string2,flags=re.I)
m = re.search("^a.+[\s]li$", string2)
print(m.group())
