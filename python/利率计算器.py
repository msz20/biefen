principal = float(input('请输入本金:'))
profit_margin = float(input('请输入利润率:(小数)'))
time = float(input('请输入年限:'))
while principal <= 0:
    print(input('本金不能为0或负数'))
    principal = float(input('请重新输入本金：'))
while profit_margin < 0 or profit_margin > 1:
    print('利润率不能为0或负数或大于1.')
    profit_margin = float(input('请重新输入利润：'))
while time <= 0:
    print(input('年限不能为0或负数.'))
    time = float(input('请重新输入年限：'))
Amount = principal * (1 + profit_margin) * time
print(f'您的总金额是{Amount}元.')