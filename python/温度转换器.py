Enter_the_data = input('请输入温度单位:(C 或 F)')
num = float(input('请输入数字:'))
unit = ()
if Enter_the_data == 'C':
    num = 32 + 1.8 * num
    unit = '华氏度'
elif Enter_the_data == 'F':
    num = num / 1.8 - 32
    unit = '摄氏度'
else:
    print('单位无效.')
print(f'温度为{round(num, 2)}{unit}.')
