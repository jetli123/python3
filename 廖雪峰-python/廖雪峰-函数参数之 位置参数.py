# -*- coding: utf-8 -*-
""""""
def power(x):
    return x * x

# 对于 power(x)函数，参数 x 就是一个位置参数。
# 现在，如果我们要计算 x3
# 怎么办？可以再定义一个 power3 函数，但是如果要计算 x4、x5 ……怎么办？我们不可能定义无限多个函数
# 可以把 power(x)修改为 power(x, n)，用来计算 x^n

def power3(x, n):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s

print(power3(2, 5))
# 修改后的 power3(x, n) 函数有两个参数：x 和 n，这两个参数都是位置参
# 数，调用函数时，传入的两个值按照位置顺序依次赋给参数 x 和 n。