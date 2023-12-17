mage = input('请输入单位(kg or lg)')
num = float(input('请输入数字:'))
new_num = ()
if mage == 'kg':
    num /= 2.88
    new_num = '磅'
elif mage == 'lg':
    num *= 2.88
    new_num = '千克'
else:
    print('单位无效.')
print(f'你的体重是{num}{new_num}')
