#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# 格式化字符串
print('Age: %s. Gender: %s' % (25, True))
print('Age: {0}. Gender: {1}' .format(25, True))
