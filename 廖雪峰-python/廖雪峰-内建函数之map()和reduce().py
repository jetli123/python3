#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# map()函数接收两个参数，一个是函数，一个是 Iterable，
# map 将传入的函数依次作用到序列的每个元素，并把结果作为新的 Iterator 返回
def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5])))
# -*-  map()函数接收两个参数，一个是函数，一个是 Iterable，-*-
                # map 将传入的函数依次作用到序列的每个元素，并把结果作为新的 Iterator 返回 -*-
                # Iterator 是惰性序列，因此通过 list()函数让它把整个序列都 计算出来并返回一个 list
# -*- [1, 4, 9, 16, 25] -*-

# -*- reduce 把一个函数作用在一个序列[x1, x2, x3, ...] 上，这个函数必须接收两个参数，
#  reduce 把结果继续和序列的下一个元
# -*- 素做累积计算，其效果就是
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

#例子1：
# 配合 map(), 把 str 转换为 int 的函数
# '13579'

def char2num(s):  # 定义函数 map() 调用
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int('13579'))

# 例子2：
# 利用 map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper()+name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 例子3：
# 利用 map 和 reduce 编写一个 str2float 函数，把字符串'123.456'转换成
# 浮点数 123.456：
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(fx, n):
        nonlocal point
        if n == -1:
            point = 1
            return fx # 返回 123
        if point == 0:  # 1*10+2， 12*10+3
            return fx * 10 + n
        else:
            point *= 10
            return fx + n / point  # 123+4/10, 123.4+5/100, 123.45+6/1000

    return reduce(to_float, nums)  # nums = [1, 2, 3, -1, 4, 5, 6]

print(str2float('123.4567'))