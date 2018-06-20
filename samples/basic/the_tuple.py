#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# cannot modify tuple:
# classmates[0] = 'Adam'


t = ('a', 'b', ['A', 'B'])
print("before = ", t)

# 虽然tuple不可变，但是tuple中引用的对象是可变的，那么是可以修改这个变量的
t[2][0] = 'apple'
t[2][1] = 'google'

print("after = ", t)

###########

