# -*- coding: utf-8 -*-
"""当我们试图加载一个模块时，Python 会在指定的路径下搜索对应的.py
文件，如果找不到，就会报错：
import mymodule
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ImportError: No module named mymodule
默认情况下， Python 解释器会搜索当前目录、所有已安装的内置模块和
第三方模块，搜索路径存放在 sys 模块的 path 变量中
"""
import sys
from pprint import pprint
pprint(sys.path)
# ['G:\\PyCharm\\python3_test\\linux_shell\\廖雪峰-python',
#  'G:\\PyCharm\\python3_test\\linux_shell',
#  'G:\\Python37\\python37.zip',
#  'G:\\Python37\\DLLs',
#  'G:\\Python37\\lib',
#  'G:\\Python37',
#  'G:\\Python37\\lib\\site-packages']

# 如果我们要添加自己的搜索目录，有两种方法
# 一是直接修改 sys.path，添加要搜索的目录：
# >>> import sys
# >>> sys.path.append('/Users/michael/my_py_scripts')

# 这种方法是在运行时修改，运行结束后失效。

# 第二种方法是设置环境变量 PYTHONPATH，该环境变量的内容会被自动添
# 加到模块搜索路径中。设置方式与设置 Path 环境变量类似。注意只需
# 要添加你自己的搜索路径，Python 自己本身的搜索路径不受影响。