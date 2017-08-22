# 只要可以调用next()的对象，就是迭代器
# 生成器都是迭代器
from collections import Iterable
# 使用Iterable来判断一个对象是否为iterable，但不能判断其是不是一个iterator
print(isinstance([1,2],Iterable))

# 使用iter方法来使list，dict，str对象变成iterator
isinstance(iter('abc'),Iterable)
