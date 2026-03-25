#想求扇形1的面积
central_angle_1 = 160
radius_1 = 30
sector_area_1 = central_angle_1 / 360 * 3.14*radius_1 ** 2
print(f"此扇形面积为: {sector_area_1}")   #print("此扇形面积为:", sector_area_1)   #print("此扇形面积为: {}".format(sector_area_1))
#相求扇形2的面积
central_angle_2 = 60
radius_2 = 23
sector_area_2 = central_angle_2 / 360 * 3.14*radius_2 ** 2
print(f"此扇形面积为: {sector_area_2}")
#想求扇形3的面积
central_angle_3 = 60
radius_3 = 23
sector_area_3 = central_angle_3 / 360 * 3.14*radius_3 ** 2
print(f"此扇形面积为: {sector_area_3}")

#DRY   don't repeat yourself

def calculate_sector_1(central_angle, radius):
    #接下来是一次写定义函数的代码
    sector_area = central_angle / 360  3.14*radius ** 2
    print(f"此扇形面积为: {sector_area}")
    return sector_area
...
sector_area_1 = calculate_sector_1(160, 30)
...
sector_area_2 = calculate_sector_1(60, 30)
...
sector_area_3 = calculate_sector_1(60, 30)