print("ciallo！我是一个求平均值的程序")
total = 0 #记录和
count = 0 #记录个数
user_input = input("请输入数字（完成所有数字后，请输入q终止程序） :")
while user_input != "q":   #!=是不等于的意思
    num = float(user_input)
    total += num    #total = total + num
    count += 1      #count = count + 1
    user_input = input("请输入数字（完成所有数字之后，请输入q终止程序") #意思是当用户输入不是q的话程序会一直向用户索要数字
if count == 0:      #不能直接result = total / count 会报错
    result = 0 
else:
    result = total / count

print("您输入的数字的平均值为" + str(result))