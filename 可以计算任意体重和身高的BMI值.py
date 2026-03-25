"""
写一个计算BMi的函数，函数名为 calculate_BMI
1可以计算任何体重和身高的BMI
2执行过程中打印一句哈，"你的BMI分类为:xx"
3返回计算出的BMI值

BMI = 体重 / (身高 ** 2)

BMI分类
偏瘦 BMI <= 18.5
正常 18.5 < BMI <= 25
偏胖 25 < BMI <= 30
飞柱 BMI > 30
"""

def calculate_BMI(weight, height):
    BMI = weight / (height ** 2)
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI <= 25:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "飞柱"
    print(f"你的BMI分类为:{category}")    #print("你的BMI分类为:{}".format(category)
    return BMI

result = calculate_BMI(66, 1.73)
print(result)