#键 : 値   key ：value
#() = 元组 tuple → 不可变                        例:t = ("张三" , 18 , 175) 一组值，靠位置分区
#[] = 列表 list → 可变 可append remove改内容       例:l = ["李四” , 16 , 156] 一组值，可增减删改
#{} = 字典 dict → key : value 键值对             例:d = {"张三" : (18 , 175) , "李四” = (16 , 156)}
slang_dict = {"助我破鼎":"源自动画电影《哪吒之魔童闹海》，用于激励自己面对挑战。"  #注意用逗号来分开
              ,"lol":"笑死"}
slang_dict["情绪价值"] = "指在社交互动中，情感支持和理解的重要性。"
slang_dict["来财"] = "与经济发展和财富积累相关，反映了年轻人的创业热情"
slang_dict["敬自己一杯"] = "表达对自己努力和成就的认可，鼓励年轻人自我肯定。"

query = input("请输入 您想要查询的流行语: ")
if query in slang_dict:
    print("您查询的" + query + "意思是")
    print(slang_dict[query])
else:
    print("您查询的流行语暂未收录")
    print("当前本词典收录词条数为: " + str(len(slang_dict)) + "条。")
    #("文字" + 10)报错，("文字" + str(10))正确