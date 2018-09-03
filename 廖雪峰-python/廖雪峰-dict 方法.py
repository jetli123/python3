# -*- coding: utf-8 -*-
""""""
# 1.get 方法
# 要避免 key 不存在的错误，有两种办法：
# 一是通过 in 判断 key 是否存在
# 二是通过 dict 提供的 get 方法，如果 key 不存在，可以返回 None，或者自己指定的 value：

a = [('a', 1), ('b', 2), ('c', 3)]
d = dict(a)
print(d)  # {'a': 1, 'b': 2, 'c': 3}
print(d.get('d'))  # 'd' key值是否存在 dict 中，不存在返回 None
# 注意：返回 None 的时候 Python 的交互式命令行不显示结果。
print(d.get('d', -1))  # 'd' key 值是否在dict 中，不存在返回指定的value : -1

# 2.pop 方法
# 要删除一个 key，用 pop(key)方法，对应的 value 也会从 dict 中删除：
d.pop('a')  # 删除 key 值 'a'
print(d)  # {'b': 2, 'c': 3}
# 请务必注意，dict 内部存放的顺序和 key 放入的顺序是没有关系的