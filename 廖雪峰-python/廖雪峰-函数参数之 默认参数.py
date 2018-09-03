# -*- coding: utf-8 -*-
# -*- 计算 x^2 函数 -*-

# 由于我们经常计算 x^2，所以，完全可以把第二个参数 n 的默认值设定为 2：
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s

# 这样，当我们调用 power(5)时，相当于调用 power(5, 2)
print(power(5))

# 默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则 Python 的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
# 变化小的参数就可以作为默认参数。

def enroll(name, gender, age=6, city='Beijing'):
    print("name:", name)
    print("gender:", gender)
    print("age:", age)
    print("city:", city)


enroll('LIli', 'F')
enroll('Cati', 'A', 9)
enroll('Natasha', 'N', city='Nanjing')

# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调
# 用 enroll('Bob', 'M', 7)，意思是，除了 name，gender 这两个参数外，
# 最后 1 个参数应用在参数 age 上，city 参数由于没有提供，仍然使用默认值。
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，
# 需要把参数名写上。比如调用 enroll('Adam', 'M', city='Tianjin')，意
# 思是，city 参数用传进去的值，其他默认参数继续使用默认值。


# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，
# 演示如下：
# -*- 函数默认参数要指向不变对象 list [] 是可变对象-*-

def add_end(L=[]):
    L.append('End')
    return L

print(add_end([1, 2]))  # [1, 2, 'End']
print(add_end())  # ['End']
print(add_end())  # ['End', 'End']
# 原因解释如下：
# Python 函数在定义的时候，默认参数 L 的值就被计算出来了，即[]，因
# 为默认参数 L 也是一个变量，它指向对象[]，每次调用该函数，如果改
# 变了 L 的内容，则下次调用时，默认参数的内容就变了，不再是函数定
# 义时的[]了。

# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
# 要修改上面的例子，我们可以用 None 这个不变对象来实现：
# -*- 修改为 L=None -*-
def add_ends(L=None):
    if L is None:
        L = []
    L.append('End')
    return L


print(add_ends())  # ['End']
print(add_ends())  # ['End']