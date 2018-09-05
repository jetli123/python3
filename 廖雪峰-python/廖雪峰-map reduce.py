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

# 配合 map(), 把 str 转换为 int 的函数
# '13579'

def fn(x, y): # 定义函数 reduce() 调用
    return x * 10 + y

def char2num(s):  # 定义函数 map() 调用
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

num = reduce(fn, map(char2num, '13579'))
print(num)