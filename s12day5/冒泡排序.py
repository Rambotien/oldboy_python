#!/usr/bin/env python
# -*- coding:utf-8 -*-
data = [10,4,33,21,1,54,3,8,11,5,22,2,1,17,13,6]
#for index,i in enumerate(data[0:-1]):
print(len(data))
count = 0
for j in range(1,len(data)): # 0 1 2 3 4 5
    for i in range(len(data)-j):
        if data[i] > data[i+1]:
            tmp = data[i+1]
            data[i+1] = data[i] #10 =>4
            data[i] = tmp # 4 => 10
        count+=1
    print(data)
print("count:",count)


'''
count = 0
data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6,34]
for i in range(len(data) - 2):
    for j in range(len(data) - i -1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j + 1], data[j]
            count += 1

    count += 1
print(data)
print(count)
'''