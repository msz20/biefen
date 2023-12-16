symbol = input('请输入计算符号')
num1 = float(input('请输入第一个数字:'))
num2 = float(input('请输入第二个数字:'))
if symbol:
    var = symbol == '+'
    symbol = num1 + num2
elif symbol:
    var = symbol == '-'
    symbol = num1 - num2
elif symbol:
    var = symbol == '*'
    symbol = num1 * num2
elif symbol:
    var = symbol == '/'
    symbol = num1 / num2
else:
    print('你所输入的运算符号无效.')
print(round(symbol))
