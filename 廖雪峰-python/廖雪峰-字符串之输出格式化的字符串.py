# -*- coding: utf-8 -*-
"""如何输出格式化的字符串。我们经常会输出类似
'亲爱的 xxx 你好！你 xx 月的话费是 xx，余额是 xx'之类的字符串，而 xxx
的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方
式"""

# 在 Python 中，采用的格式化方式和 C 语言是一致的，用%实现，举例如下：
print('Hello, %s' % 'world')

# %运算符就是用来格式化字符串的。在字符串内部，%s
# 表示用字符串替换，%d 表示用整数替换，有几个%?占位符，后面就跟几
# 个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略