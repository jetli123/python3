# -*- coding: utf-8 -*-
""""""
# Python 内置的一种数据类型是列表：list。list 是一种有序的集合，可以
# 随时添加和删除其中的元素。

# 用索引来访问 list 中每一个位置的元素，记得索引是从 0 开始的
# len() 函数，获得list 元素个数 len(classmates)
# 当索引超出了范围时，Python 会报一个 IndexError 错误，所以，要确保
# 索引不要越界，记得最后一个元素的索引是 len(classmates) - 1。

# 创建列表函数： list()
m = list([1, 2, 3])
print(m)  # [1, 2, 3]

# 1.append() 方法
# list 是一个可变的有序表，所以，可以往 list 中追加元素到末尾：
a = ['a', 'b', 'c']
classmates = list()
classmates.append(7)
a.append('d')
print(classmates)  # [7]
print(a)  # ['a', 'b', 'c', 'd']

# 2.insert() 方法
# 把元素插入到指定的位置，比如索引号为 1 的位置：
classmates.insert(1, 3)
print(classmates)  # [7, 3]

# 3.pop() 方法
# 删除list 末尾元素
classmates.pop()
print(classmates)  # [7]

# pop(i) 删除指定位置的元素 ，i 是索引位置
classmates.pop(0)
print(classmates)  # []

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
# list 里面的元素的数据类型也可以不同，比如：
# >>> L = ['Apple', 123, True]
# list 元素也可以是另一个 list，比如：
# >>> s = ['python', 'java', ['asp', 'php'], 'scheme']
# 要拿到'php'可以写 p[1]或者 s[2][1]，因此 s 可以看成是一个二维数组

# 4.sort()方法，在原位置对列表进行排序，改变原列表
x = [3, 1, 5, 7]
x.sort()
print(x)  # [1, 3, 5, 7]

# 5.sorted()方法， 获取已排序的列表副本，不改变原列表
x = [3, 1, 4, 2]
y = sorted(x)
print(y)  # [1, 2, 3, 4]
print(x)  # [3, 1, 4, 2]  原列表不变。

# 6.extend() 方法， 在列表末尾一次追加另一个序列中的值,改变原列表。
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]

# 7.index() 方法 ，从列表中找出某个值第一个匹配项的索引位置。
c = [8, 9, 0]
print(c.index(0))  # 所因位置： 2

# 8.remove() 方法， 移除列表中某个值的第一个匹配项（如果有相同的多个值）
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('to')
print(x)  # ['be', 'or', 'not', 'to', 'be']

# 9.count() 方法， 统计某个元素在列表中出现的次数
x = ['to', 'be', 'or', 'not', 'to', 'be']
print(x.count('be'))  # 2

# 10.reverse() 方法，将列表中的元素反向存放
x = [1, 2, 3]
x.reverse()
print(x) # [3, 2, 1]