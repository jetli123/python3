# -*- coding: utf-8 -*-
"""
另一种有序列表叫元组：tuple。tuple 和 list 非常类似，但是 tuple 一旦
初始化就不能修改，比如同样是列出同学的名字：
"""
# 创建元组函数
# tuple() 函数, 与list 函数基本一样：以一个序列作为参数，并把它转换为元组
a = tuple([1, 2, 3])
print(a)  # (1, 2, 3)

# 获取元素的方法和 list 是一样的，你可以正常地使用 classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 因为 tuple 不可变，所以代码更安全
a = ('Michael', 'Bob', 'Tracy')
print(a[1])  # Bob


# “可变的”tuple
# >>> t = ('a', 'b', ['A', 'B'])
# >>> t[2][0] = 'X'
# >>> t[2][1] = 'Y'
# >>> t
# ('a', 'b', ['X', 'Y'])
# 其实变的不是 tuple 的元素，而是 list 的元素。tuple 一开始指向的 list 并没有改成别的 list，所以，tuple
# 所谓的“不变”是说，tuple 的每个元素，指向永远不变。
# 即：
# 指向'a'，就不能改成指向'b'，指向一个 list，就不能改成指向其他对象，但指向的这个 list 本身是可变的！


# 小结
# list 和 tuple 是 Python 内置的有序集合，一个可变，一个不可变。