"""读取模式"""
open("/usr/demo/data.txt", "r", encoding= "utf-8")    #"r"是读取模式(只读) "w"是写入模式(只写) 不写时默认读取模式,encording是编码方式 一般都是UTF-8

f = open("/usr/demo/data.txt", "r", encoding= "utf-8")
print(f.read())
"""
在文件特别大的情况下，不推荐用　①read　方法，全读容易爆了
如果只想都一部分，可以给read传一个 读多少字节"""
print(f.read(10)) # 读第1-10个字节的文件内容
print(f.read(10)) # 读11-20个字节的内容，下一次调用时候，会继续往后读

"""也可以用　②readline　方法，就读一行"""
f = open("/usr/demo/data.txt", "r", encoding= "utf-8")
print(f.readline()) # 会读一行文件内容，并打印
print(f.readline()) # 会读一行文件内容，并打印
"""
readline会根据 换行符 来判断什么时候算本行结尾
如果到达结尾，readline会和read一样返回空字符串，表示后面没有内容了"""

f = open("/usr/demo/data.txt", "r", encoding= "utf-8")
line = f.readline()
while line != "":       #当line不等于 空行 时，继续打印读取下一行
    print(line)         #意思就是要是为空行的时候就停
    line = f.readline()

"""也可以用　③readlines　方法
readlines会读取全部内容，并返回每行组成的字符串列表
一般会和for循环结合使用"""
# read():把整个文件读成一个大字符串  readlines:把整个文件读成 按行隔开的列表(list)
f = open("/usr/demo/data.txt", "r", encoding= "utf-8")
lines = f.readlines()
for line in lines
    print(line)

"""文件后就要关闭文件""" 

f = open("./data.txt")
print(f.read())
f.close()   #关闭文件，释放资源

"""写入模式"""
with open("./unknown.txt", "w", encoding="utf-8") as f:    #如果文件不存在，程序就会自动创建个文件叫那个名字然后输入. 如果文件已经存在，就会把原本的文件内容清空！
    f.write("hello\n")   #如果要换行的话要自己加
    f.writh("Yoooo")

"""附加模式"""
with open("./unknown.txt", "a", encoding="utf-8") as f:    #如果只是想在原文件的基础上加东西，就用"a"
    f.write("hello\n")
    f.writh("Yoooo")