#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

print('------for key in d---------')

# 通过key的方式
for key in d:
    print(key, "=", d[key])

print('------for k, v in d.items()---------')

'''
https://docs.python.org/3/tutorial/datastructures.html#tut-loopidioms
直接key,value
'''
for k, v in d.items():
    print(k, "=", v)
