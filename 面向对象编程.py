#接下来定义一个自己的类
#定义普通变量是用下划线_ 例子(user_name)
#python在定义类名的时候Pascal命名法，特点是用首字母大写来分隔单词

#class 定义对象
#def 定义功能
#return 返回结果


class CuteCat:
    def __init__(self, cat_name, cat_age, cat_color):
        #self 表示 这只猫自己， 把传进来的名字，年龄，颜色， 保存到这只猫身上
        self.name = cat_name     #猫的名字
        self.age = cat_age       #猫的年龄
        self.color = cat_color   #猫的颜色

cat1 = CuteCat("Jojo", 2, "橙色")     #创建一只猫对象 ，只是用 = 传参数， 不是" : " 的意思
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，颜色是{cat1.color}")  #f字符串: 把变量放进到字符串里打印

"""
演练
"""

class CuteCat:    #通过class 可以创建一个类
    def __init__(self, cat_name, cat_age, cat_color):    #通过__init__这个构造方法，可以定义对象拥有那儿些属性
        self.name = cat_name   # . 就是 的 的意思
        self.age = cat_age
        self.color = cat_color

    def speak(self):    #和__init__一样 第一个参数一样 用来表示参数自身
        print("喵" * self.age)

    def think(self, content):
        print(f"小猫{self.name}在思考{content}")

cat1 = CuteCat("Jojo", 1, "橙色")    #用过class的名字后面加括号，可以调用__init__来创建新对象，并且把对应属性进行赋值
cat1.think("现在去抓沙发还是去撕纸箱")