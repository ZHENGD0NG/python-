#一个可以测量天空亮度的函数 measure_brightness
#希望一直捕捉照片，需要运到循环 （for循环 / while循环）
for i in range(100):
    if measure_brightness() >= 500:
        # 拍照片
        take_photo()    #循环（0→99）100次

while measure_brightness() >= 500:
    take_photo()



#循环下面的list
list1 = ["你", "好", "吗", "兄", "弟"]
#第一种方法
for char in list1:
    print(char)
#第二种方法
for i in range(len(list1)):
    print(list1[i])
#第三种方法
i = 0
while i < len(list1):
    print(list1[i])
    i = i + 1
