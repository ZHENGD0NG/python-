#import语句
import statistics
print(statistics.median([1,2,3,4,5,6,7,8,9]))
print(statistics.mean([1,2,3,4,5,6,7,8,9]))

#from...import...语句
from statistics import median, mean
print(median([1,2,3,4,5,6,7,8,9]))
print(mean({1,2,3,4,5,6,7,8,9}))

#from...import*    用*的时候，模块的所有函数或者变量都会被引入
from statistics import*
print(median({1,2,3,4,5,6,7,8,9}))
print(mean([1,2,3,4,5,6,7,8,9]))

"""
可以从pypi.org这个网站对第三方库进行搜索
安装的话去到终端，输入 pip install + 名字
安装成功后就可以用 import 引用进来
"""