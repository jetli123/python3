# -*- coding: utf-8 -*-
""""""
# 和 list 比较，dict 有以下几个特点：
# 1.  查找和插入的速度极快，不会随着 key 的增加而增加；
# 2.  需要占用大量的内存，内存浪费多。
# 而 list 相反：
# 1.  查找和插入的时间随着元素的增加而增加；
# 2.  占用空间小，浪费内存很少。

# 所以，dict 是用空间来换取时间的一种方法。
# dict 可以用在需要高速查找的很多地方，在 Python 代码中几乎无处不在，
# 正确使用 dict 非常重要，需要牢记的第一条就是 dict 的 key 必须是不可变对象。

# 这是因为 dict 根据 key 来计算 value 的存储位置，如果每次计算相同的
# key 得出的结果不同，那 dict 内部就完全混乱了。这个通过 key 计算位
# 置的算法称为哈希算法（Hash）

# 要保证 hash 的正确性，作为 key 的对象就不能变。在 Python 中，字符
# 串、整数等都是不可变的，因此，可以放心地作为 key。而 list 是可变
# 的，就不能作为 key：
d = dict()
key = [1, 2, 3]
d[key] = 'a list'
print(d)
# Traceback (most recent call last):
#    File "1.py", line 23, in <module>
# TypeError: unhashable type: 'list
