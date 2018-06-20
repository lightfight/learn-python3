#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 计算1+2+3+...+100:
# 因为sum是一个常用的库方法名，所以有提示
s = 0
n = 1
while n <= 100:
    s += n
    n = n + 1
print(s)

# 计算1x2x3x...x100:
acc = 1
n = 1
while n <= 5:
    acc = acc * n
    n = n + 1
print(acc)

'''
 我是多行注释
'''

t = 1
n = 1
while n < 6:
    t *= n
    n += 1
print(t)
