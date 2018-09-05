# -*- coding: utf-8 -*-
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。


def now():
    print('时间：2017-11-04')

f = now  # 函数 now 作为对象 赋值给 变量 f
f()

# 函数对象有一个__name__属性，可以拿到函数的名字：
print('now的__name__属性为：', now.__name__)
print('函数f()的name属性为：', f.__name__)


# 现在，假设我们要增强 now()函数的功能，比如，在函数调用前后自动
# 打印日志，但又不希望修改 now()函数的定义，这种在代码运行期间动
# 态增加功能的方式，称之为“装饰器”（Decorator）。


def log(func):
    def wrapper(*args, **kw):
         print('call %s():' % func.__name__)
         return func(*args, **kw)
    return wrapper


@log
def now():
    print('2017-11-22')
# 调用 now()函数，不仅会运行 now()函数本身，还会在运行 now()函数前
# 打印一行日志：

now()
# call now():
# 2017-11-22

# 把@log 放到 now()函数的定义处，相当于执行了语句：
# now = log(now)

# 由于 log()是一个 decorator，返回一个函数，所以，原来的 now()函数仍
# 然存在，只是现在同名的 now 变量指向了新的函数，于是调用 now()将
# 执行新函数，即在 log()函数中返回的 wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接
# 受任意参数的调用。在 wrapper()函数内，首先打印日志，再紧接着调用原始函数