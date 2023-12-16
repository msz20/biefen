import math

x = 122.42422
print(math.ceil(x))

y = 1224.12424112
print(math.floor(y))
# 圆的周长2piR
mmm = float(input('请输入圆的半径：'))
a = 2 * math.pi * mmm
print(round(a, 2))
# 圆的面积
races = float(input('请输入圆的半径：'))
a = math.pi * pow(races, 2)
print(round(a, 2))
