# -*- coding: utf-8 -*-
""""""
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对
# 象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证
# 了不可变对象本身永远是不可变的
# 1.replace() 方法：
# >>> a = 'abc'
# >>> b = a.replace('a', 'A')
# >>> b
# 'Abc'
# >>> a
# 'abc'

# 要始终牢记的是，a 是变量，而'abc'才是字符串对象！有些时候，我们
# 经常说，对象 a 的内容是'abc'，但其实是指，a 本身是一个变量，它指
# 向的对象的内容才是'abc'：

# 2.find() 方法
# find 方法：在字符串中查找子串，返回子串开头所在的位置的最左端索引，没有返回 -1
# >>>names = "Month Python's Flying Circus"
# >>>names.find("Month")
# 0
# >>>names.find("Python")
# 6

# find 方法2：使用起始点和结束点，查找子串
# >>>aa = '$$$ Get !!! $$$'
# >>>aa.find('$$$',1)  --添加了起始点，从索引为1 的位置找出 $$$ 字符串
# 12
# >>>aa.find('!!!', 4, 13)  --添加 起始点和结束点
# 8

# 3.join() 方法：split 的逆方法，连接序列中的元素，序列必须是字符串
seq = ['1', '2', '3', '4']
ab = '+'
print(ab.join(seq)) # '1+2+3+4'

seq = '', 'usr', 'bin', 'env'
print('/'.join(seq)) # '/usr/bin/env'

# 4.split() 方法： join 方法的逆方法，将字符串分割成序列
a = '1+2+3+4'
print(a.split('+'))  # ['1', '2', '3', '4']
seq = '/usr/bin/env'
print(seq.split('/'))  # ['', 'usr', 'bin', 'env']