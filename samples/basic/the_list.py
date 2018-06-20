#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])

# 如果越界了就取最后一个
print('classmates[-1] =', classmates[-1])

# 取数组中的最后一个
print('classmates[len(classmates) - 1] =', classmates[len(classmates) - 1])

classmates.pop()
print('classmates =', classmates)

# IndexError: list index out of range
# print('classmates =', classmates[10])

# 二位数组
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s)

# 取得php
print(s[2][1])

