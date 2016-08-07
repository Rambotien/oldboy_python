#!/usr/bin/env python
"""
all_item = 95
pager = 10
result = all_item.__divmod__(10)
print(result)
"""
age = 18
#result = age.__eq__(19)
#print(result)
#print(type(age))
#result = age.__float__()
#print(type(result))
"""
age = 5
result = age.__floordiv__(6)
print(result)
print(5//6)

age = 19
age = int(19)
# 执行int类的__init__方法
age.__add__(1,23)

"""
#name = 'eric'

#name = str('eric') # str类的__init__
#print(type(name))
#print(dir(name))

#result = name.__contains__('er6')
#result = 'er6' in name
#print(result)

#name = 'Eric'
#result = name.casefold()
#print(result)
#print '*****************888***************'
#result = name.center(20,'*')
#print(result)

#name = 'asdf;luourtkapsdiufasdf'
#result = name.count('df',9,10)
#print(result)

#name = '李杰'
#result = name.encode('gbk')
#print(result)

#name = 'alex'
#result = name.endswith('e',0,3)
#print(result)
"""
name = 'a\tlex'
result = name.expandtabs()
print(len(result))
"""

"""
name = 'alex'
#result = name.find('ex')
result = name.index('y')
print(result)
"""
#name = "alex {0} as {1}"
#result = name.format('sb','eric')
#print(result)
#name = "alex {name} as {id}"
#result = name.format(name='sb', id='eric')
#print(result)
"""
li = ['s','b','a','l','e','x']
result = "-".join(li)
print(result)
"""
#name = 'alexissb'
#result = name.partition('is')
#print(result)
#name = 'alexaisasab'
#result = name.replace('a', 'o',2)
#print(result)
name = """
ak
bb
cc"""

"""
#result = name.splitlines()
result = name.split('\n')
print(result)
"""



"""
import contextlib

@contextlib.contextmanager
def show():
    print('123')
    yield
    print('456')

with show():
    print('99999')



#with open('h.log') as f:
#    f.write()
"""
#li = list([1,2,3])
#print(li)
#li.extend([11,22])
#li.extend((11, 22, ))
#li.insert(0,'aelx')
#ret = li.pop(0)
#print(li)
#print(ret)
#tu = (11,22,34,)
#tu = tuple((11,22,34,))
#tu = tuple([11,22,34,])

#dic = {'k1':'v1','k2':'v'}
#dic = dict(k1='v1',k2='v2')
#new_dict = dic.fromkeys(['k1','k2','k3'],'v1')
#print(new_dict)

#dic = {'k1':'v1','k2':'v2'}
#print(dic['k1'])
#print(dic['k2'])
#print(dic['k3'])
#print(dic.get('k1'))
#print(dic.get('k2','alex'))
#print(dic.get('k3','alex'))


"""
print(dic.keys())
print(dic.values())
print(dic.items())
for k in dic.keys():
    print(k)
for v in dic.values():
    print(v)
for k,v in dic.items():
    print(k,v)
"""
#dic.pop('k1')


#dic.popitem()
#print(dic)
#dic['k4'] = 123
#dic.setdefault('k4',123)
#print(dic)

#dic = {'k1':'v1','k2':'v2'}
#ret = dic.update({'k3':123})
#print(dic)
"""
有如下值集合
[11,22,33,44,55,66,77,88,99,90...]，
将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
即： {'k1': 大于66 , 'k2': 小于等于66}

all_list = [11,22,33,44,55,66,77,88,99,90]
dic = {}
l1 = []
l2 = []
for i in all_list:
    if i>66:
        l1.append(i)
    else:
        l2.append(i)
dic['k1'] = l1
dic['k2'] = l2
"""
#{'k1':[66,99888,777,66],'k2':[11,22,33,44]}
dic = {}
all_list = [11,22,33,44,55,66,77,88,99,90]
for i in all_list:
    if i>66:
        if "k1" in dic.keys():
            dic['k1'].append(i)
        else:
            dic['k1'] = [i, ]
    else:
        #dic = {'k2':[11,22,]}
        if "k2" in dic.keys():
            dic['k2'].append(i)
        else:
            dic['k2'] = [i, ]
            #dic = {}
            #dic = {'k2':[11,]}
