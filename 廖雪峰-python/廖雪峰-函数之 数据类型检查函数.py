# -*- coding: utf-8 -*-
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# -*- 调用函数 my_abs ，x 为负数-*-
print(my_abs(-109))
# 测试 x 为字符串，输出 TypeError -*-
print(my_abs('-109'))