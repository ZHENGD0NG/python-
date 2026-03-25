# f = open(r"C:\Users\ri\OneDrive\Desktop\python_practice\Data.txt", "r", encoding="utf-8")
# #打印前面的r的意思是"原始字符串" 别解析\U，按原样读取
# content = f.read()
# print(content)
# f.close()

"""不想在结尾 f.close 的话"""

with open(r"C:\Users\ri\OneDrive\Desktop\python_practice\Data.txt", "r", encoding="utf-8") as f:
    # content = f.read()
    # print(content)
    #
    # print(f.readline())    #两行代码只读取两行
    # print(f.readline())

    #print(f.readlines())    #按列表的方式输入

    lines = f.readlines()
    for line in lines:
        print(line)
