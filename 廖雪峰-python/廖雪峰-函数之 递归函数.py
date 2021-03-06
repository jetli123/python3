# -*- coding: utf-8 -*-
"""
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，
这个函数就是递归函数。
"""
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print(fact(5))

# -*- 如果我们计算 fact(5)，可以根据函数定义看到计算过程如下： -*-
#===> fact(5)
#===> 5 * fact(4)
#===> 5 * (4 * fact(3))
#===> 5 * (4 * (3 * fact(2)))
#===> 5 * (4 * (3 * (2 * fact(1))))
#===> 5 * (4 * (3 * (2 * 1)))
#===> 5 * (4 * (3 * 2))
#===> 5 * (4 * 6)
#===> 5 * 24
#===> 120

#-*- 判断一个对象是可迭代对象的方法是通过 collections 模块的 Iterable 类型判断： -*-
from collections import Iterable

print(isinstance('abc', Iterable))


# -*- 内置的 enumerate 函数可以把一个 list 变成索引-元素对，这样就可以在 for 循环中同时迭代索引和元素本身 -*-
def tes(lis):
    for i, value in enumerate(lis):
        print(i, value)

cc = ['A', 'B', 'C']
tes(cc)


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(4, 'A', 'B', 'C')
