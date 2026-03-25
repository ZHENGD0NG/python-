contacts = ["老余", "老林", "老陈", "老曾", "老李", "老张"]
for name in contacts:
    message_content = name + ":岁月之乐，点翠画柳喜开颜。"\
                             "云开雾散，良辰美景共团圆。祝福" + name + \
                      "及家人新年快乐，平安顺遂，虎年大吉！"
    print(message_content)      #如果是发送的话使用 send_message(name, message_content)

#############################################################################################

#写一个鼠年就是鼠年大吉，兔年就是兔年大吉的代码，一辈子都用这个祝福内容
contacts = ["老余", "老林", "老陈", "老曾", "老李", "老张"]
year = "虎"
for name in contacts:
    message_content ="""
    律回春渐。新年开启。
    新岁甫至，福气东来。
    金""" + year + """贺岁，欢乐祥瑞。
    金""" + year + """敲门，五福临门。
    给""" + name + """及家人拜年啦！
    新春快乐，""" + year + """年大吉！"""
    print(name, message_content)
#但是这种非常不直观和连贯

#比如说下面这种用.format方法
for name in contacts:
    message_content ="""
    律回春渐。新年开启。
    新岁甫至，福气东来。
    金{0}贺岁，欢乐祥瑞。    
    金{0}敲门，五福临门。
    给{1}及家人拜年啦！
    新春快乐，{0}年大吉！
    """.format(year, name)    #{}表示会被替换的位置，里面的数字表示会用format里面的第几个参数进行替换，0表示第一个参数year，1表示第二个参数name

#.format还可以根据关键词来指定进行替换的对象
    message_content ="""
    律回春渐。新年开启。
    新岁甫至，福气东来。
    金{current_year}贺岁，欢乐祥瑞。    
    金{current_year}敲门，五福临门。
    给{receiver_name}及家人拜年啦！
    新春快乐，{current_year}年大吉！
    """.format(current_year = year, receiver_name = name)

#还可以用f-字符串
    name = "老林"
    year = "虎"
    message_content =f"""
    律回春渐。新年开启。
    新岁甫至，福气东来。
    金{year}贺岁，欢乐祥瑞。    
    金{year}敲门，五福临门。
    给{name}及家人拜年啦！
    新春快乐，{year}年大吉！
    """

#
gpa_dict = {"小明":3.251, "小花":3.869, "小李":2.683, "小张":3.685}
for name, gpa in gpa_dict.items():
    print("{0}你好，你当前的绩点为:{1}".format(name, gpa))
    #还可以用 :.2f 来指定浮点数在格式化时保留几位小数，这个是保留两位小数
    print("{0}你好，你当前的绩点为:{1:.2f}".format(name, gpa))

    #用f-字符串的时候也是一样
    print(f"{name}你好，你当前的绩点为:{gpa:.2f}")