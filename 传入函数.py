# 想搞一个输入就知道几的几次方是多少的计算函数
def calculate_and_print(num,  power):    # num_底数 power_次方数(指数)
    if power == 2:
        result = num * num
    elif power == 3:
        result = num * num * num
    else:
        print("只支持计算二次方和三次方")
        return
    print(f"""| 数字参数 | {num}
    | 计算结果 | {result}""")

calculate_and_print(3, 3)

# 可以把计算的函数，直接作为参数 看下面 ⬇
# 高阶函数，非常具有灵活性
def calculate_and_print(num, calculator):   # num是输入的数字，calculate是一个函数，可以在后面自己加
    result = calculator(num)    # 把输入的数字放进函数calculator里计算
    print(f"""
    | 数字参数 |{num}
    | 计算结果 |{result}""")

#下面三个函数只是不同的计算方式
def calculate_square(num):    # square 乘方
    return num * num

def calculate_cube(num):    # cube 三次方
    return num * num * num

def calculate__plus_10(num):
    return num + 10

def calculate_times_5(num):
    return num * 5

calculate_and_print(3, calculate_square)    #calculate_square是作为参数的函数，直接用函数名进行传入，表示用这个函数本身，后面不要带（ ）或者 参数
calculate_and_print(7, calculate_cube)

# 有时候要传的函数不常用 想即用即仍 就用_匿名函数_以lambda这个关键字开始

#正常写是这样
def calculate_times_5(num):
    return num * 5
#匿名函数写法
lambda num: num * 5    #关键字 函数参数: 函数返回的表达式

print("lambda num1, num2: num1 + num2)(2,3)")