#!/usr/bin/env python
# -*- coding:utf-8 -*-
from  multiprocessing import Process,Pool,freeze_support
import time

def Foo(i):
    time.sleep(2)
    print('exec...')
    return i+100

def Bar(arg):
    print('-->exec done:',arg)


if __name__ == '__main__':
    freeze_support()
    pool = Pool(3)
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,),callback=Bar)
        #pool.apply(func=Foo, args=(i,))
    print('end')
    pool.close()
    #pool.join()#进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。