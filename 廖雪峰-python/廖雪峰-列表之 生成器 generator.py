# -*- coding: utf-8 -*-

# 受到内存限制，
# 列表容量肯定是有限的。而且，创建一个包含 100 万个元素的列表，不
# 仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面
# 绝大多数元素占用的空间都白白浪费了。

# 在 Python 中，一边循环一边计算的机制，称为生成器: generator

print([pow(x, 2) for x in range(1, 10)]) # -*- 结果是 list -*-
g = (y * y for y in range(1, 10))  # -*- 结果是 generator -*-
print(next(g))  # 打印 generator 通过 next() 函数
print(next(g))
print(next(g))
# 正确方式通过 for 循环 迭代 generator
for n in g:
    print(n)

# 这就是定义 generator 的另一种方法。如果一个函数定义中包含 yield 关
# 键字，那么这个函数就不再是一个普通函数，而是一个 generator：
# 斐波拉契函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

g = fib(6)
print(g)  # <generator object fib at 0x0000000002138048>
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return  value:', e.value)
        break

