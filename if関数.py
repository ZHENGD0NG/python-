mood_index = int(input("对象的心情指数是： "))
if mood_index >= 60:       #input関数返回的是字符串 所以和数字60比的话就要把mood_index换成数字
    print("恭喜，今晚可以打游戏，去吧皮卡丘! ") #if后面要有缩进，就是要有前面4个空格
else:      # mood_index < 60的时候
    print("为了自个儿小命，还是别打了。 ")