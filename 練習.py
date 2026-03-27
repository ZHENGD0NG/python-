#对字符串求长度 （字符个数）len
s = "hello world!"
print(len(s))

#通过索引 获取单个字符
print(s[0]) #程序世界是从0开始数
print(s[len(s)-1]) #字符串长度-1  意思就是 print(s[11])

#布尔类型 bool 用来表示“真假/是非”的数据类型
b1 = True
b2 = False #一定要大写

#空值类型
n = None

#type函数    看一个值/变量的“数据类型”(问这玩意到底是int还是str还是list)
print(type(s))
print(type(b1))
print(type(n))
print(type(1.5))

#input()    从用户那里获取输入
#input("你的年龄")   #屏幕显示你的年龄  然后用户输入 然后回车输入结束
user_age = input("你的年龄") #input() 的返回值永远是字符串（str）
print("知道了，你今年" + user_age + "岁了！")

user_age = int(input("请输入您的年龄: "))
user_age_after_10_year = user_age + 10
print("您十年后会是" + str(user_age_after_10_year) + "岁") #打印的必须是字符串

#比较运算符
# == #等于号
# != #不等于好
# >  >=  #大于 大于等于
# <  <=  #小于 小于等于