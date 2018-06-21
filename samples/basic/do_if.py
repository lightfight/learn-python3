#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
# age = int(input('Input your age: '))
#
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')


# 将if和while结合起来
# 判断年龄的范围
def judge(years):
    if years >= 18:
        print('adult')
    elif years >= 6:
        print('teenager')
    else:
        print('kid')


# 不停的接收控制台的输入
while True:
    age = int(input('Input your age: '))
    judge(age)








