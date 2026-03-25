#键 : 値   key ：value
#() = 元组 tuple → 不可变                        例:t = ("张三" , 18 , 175) 一组值，靠位置分区
#[] = 列表 list → 可变 可append remove改内容       例:l = ["李四” , 16 , 156] 一组值，可增减删改
#{} = 字典 dict → key : value 键值对             例:d = {"张三" : (18 , 175) , "李四” = (16 , 156)}
temperature_dict = {
    "111":36.4,
    "112":36.6,
    "113":36.2,
    "114":37.0,
    "115":36.8,
    "116":39.9,
    "117":38.9
    }
#temperature_dict.key()   返回: 所有键
#temperature_dict.values()     所有值
#temperature_dict.items()      所有键值对
for staff_id, temperature in temperature_dict.items():
    if temperature >= 38:
        print(staff_id)
        print(temperature)
        print("完球了")


range(5, 10)   #整数数列    5, 6, 7, 8 ,9  没有10
for i in range(5, 10):
    print(i)

range(5, 10, 2) #(起始值 默认0， 结束值 ，每次跨几个数字） 不指名的时候默认为1


#高斯 总数 = （首+尾）项数 /2
total = 0
for i in range(1, 101):
    total = total + i
print(total)