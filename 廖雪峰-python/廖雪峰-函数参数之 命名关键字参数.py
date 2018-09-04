# -*- coding: utf-8 -*-
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# -*- 但是调用者仍可以传入不受限制的关键字参数 -*-
person('Jack', 22, city='Beijing', addr='Chaoyang', zipcode=123456)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接
# 收 city 和 job 作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city='Shanghai', job):    # Python 2.7 不支持，等待升级到Python3
   print(name, age, city, job)
   # 和关键字参数 ** kw
   # 不同，命名关键字参数需要一个特殊分隔符 *，*后面
   # 的参数被视为命名关键字参数。
person('Michel', 10, job='Engineer')
person('Shift', 80, city='Beijing', job='Teacher')


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参
# 数名，调用将报错：
# >>> person('Jack', 24, 'Beijing', 'Engineer')
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: person() takes 2 positional arguments but 4 were given
# 由于调用时缺少参数名 city 和 job， Python 解释器把这 4 个参数均视为
# 位置参数，但 person()函数仅接受 2 个位置参数


# 使用命名关键字参数时，要特别注意，*不是参数，而是特殊分隔符。
# 如果缺少*，Python 解释器将无法识别位置参数和命名关键字参数：
# def person(name, age, city, job):
#     缺少 *，city 和 job 被视为位置参数
    # pass

# 在 Python 中定义函数，可以用必选参数、默认参数、可变参数、关键
# 字参数和命名关键字参数，这 5 种参数都可以组合使用，除了可变参数
# 无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必
# 选参数、默认参数、可变参数/命名关键字参数和关键字参数。
# -*- 参数组合 使用 -*-
# 1.位置参数，默认参数，可变参数，关键字参数组合
def f1(name, old, size=0, *args, **kw):
    print('name =', name, 'old =', old, 'size =', size, 'args =', args, 'kw =', kw)

# 2.位置参数，默认参数，命名关键字参数，关键字参数组合
def f2(name, old, size=0, *, city, **kw):
    print('name=', name, 'old=', old, 'size=', size, 'city=', city, 'kw=', kw)

dd = {'ages': 22, 'address': 'Beijing'}
cc = (1, 2, 3, 4)
f1('Jack', 23, 330, *cc, **dd)
# name = Jack old = 23 size = 330 args = (1, 2, 3, 4) kw = {'ages': 22, 'address': 'Beijing'}
f2('Jack', 23, 340, city='Beijing', **dd)
# name= Jack old= 23 size= 340 city= Beijing kw= {'ages': 22, 'address': 'Beijing'}

# 所以，对于任意函数，都可以通过类似 func(*args, **kw)的形式调用它，
# 无论它的参数是如何定义的。
aa = ('Jack', 100, 270)
f1(*cc, **dd)
# name = 1 old = 2 size = 3 args = (4,) kw = {'ages': 22, 'address': 'Beijing'}
f2(*aa, city='Beijing', **dd)
# name= Jack old= 100 size= 270 city= Beijing kw= {'ages': 22, 'address': 'Beijing'}