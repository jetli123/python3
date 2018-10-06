#/usr/bin/env python
# -*- coding: utf-8 -*-

# Mrjob 是一个编写MapReduce 任务的开源Python框架，它实际上对 Hadoop Streaming的命令行进行了封装，因此接触不到Hadoop
# 的数据流命令行，使我们可以更轻松、快速编写MapReduce任务。
# Mrjob具有如下特点：
# 1.代码简洁，map及reduce 函数通过一个Python文件就可以搞定；
# 2.支持多步骤的MapReduce任务工作流；
# 3.支持多种运行方式，包括内嵌方式、本地环境、Hadoop、远程亚马逊；
# 4.支持亚马逊网络数据分析服务 Elastic MapReduce（EMR）；
# 5.调试方便，无需任何环境支持。

# Mrjob 源码下载地址：https://github.com/yelp/mrjob
# 回到实现一个统计文本文件 input.txt 中所有单词出现的词频功能，Mrjob通过mapper() 与 reducer()方法实现了MR操作
# 实现代码如下：
from mrjob.job import MRJob

class MRWordCounter(MRJob):

    def mapper(self, key, line):
        for word in line.split():
            yield word, 1
    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRWordCounter.run()