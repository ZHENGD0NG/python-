shopping_list = []
shopping_list.append("键盘")
shopping_list.append("键帽")
shopping_list.append("键帽")
shopping_list.append("马桶刷子") #添加
shopping_list.remove("马桶刷子") #减少
shopping_list.append("音响")
shopping_list.append("电竞椅")
shopping_list[1] = "硬盘" #0是键盘，1是键帽，2也是键帽，把1换成硬盘

print(shopping_list)
print(len(shopping_list))   #len元素看有多少个元素
print(shopping_list[0])  #看0是什么元素

price = [799, 1024, 200, 800]
max_price = max(price) #用max函数 min函数 获取最大小
min_price = min(price)
sorted_price = sorted(price)  #排序一下价格
print(max_price)
print(min_price)
print(sorted_price)