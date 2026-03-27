import math                            # 导入数学库（为了用 sqrt 开根号）

# 2的三次方 = 2**3

a = -1
b = -2
c = 3                                  # 你手动给了 a,b,c 三个系数
delta = b ** 2 - 4 * a * c             # 判别式 Δ = b² - 4ac
# print((-b + math.sqrt(delta))/(2 * a))
print((-b - math.sqrt(delta))/(2 * a))