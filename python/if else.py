for_sale = True
if for_sale:
    print('已出售')
else:
    print('正在出售')
age = int(input('请输入你的年龄:'))
if age:
    var = age >= 18
    print('你可以注册')

elif age:
    var = age <= 100
    print('你的年龄太大无法注册.')
elif age:
    var = age < 0
    print('你还没出生.')
else:
    var = age > 18
    print('你的年龄不够大.')
