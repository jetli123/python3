# -*- coding: utf-8 -*-
"""在 Python 函数中，还可以定义可变参数。顾名思义，可变参数就是传
入的参数个数是可变的，可以是 1 个、2 个到任意个，还可以是 0 个。
我们以数学题为例子，给定一组数字 a，b，c……，请计算 a^2 + b^2+ c^2+ ……。
要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，
我们首先想到可以把 a，b，c……作为一个 list 或 tuple 传进来，这样，函数可以定义如下：
"""
# 调用的时候，需要先组装出一个 list 或 tuple -*-
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([2, 3]))  # -*- 参数为 list -*-
print(calc((3, 2)))  # -*- 参数为 tuple -*-

# -*- 如果调用函数的方式简化成 calc(1, 2, 3) 那么改成可变参数 *numbers,
# -*- 可变参数允许你传入 0 个或任意个参数，这些可变参数在函数调用时自动组装为一个 tuple

def cala(*nums):
    sums = 0
    for x in nums:
        sums = sums + x * x
    return sums

print(cala(1, 2, 3))

# -*- 如果已经有一个 list or tuple 调用可变参数 -*-
numss = [1, 2, 3, 4]  # -*- list -*-
print(cala(*numss))
nba = (2, 4, 6)       # -*- tuple -*-
print(cala(*nba))

