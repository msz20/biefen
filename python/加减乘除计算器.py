symbol = input('请输入计算符号')
num1 = float(input('请输入第一个数字'))
num2 = float(input('请输入第二个数字'))
small = ()
if symbol == '+':
    small = num1 + num2
elif symbol == '-':
    small = num1 - num2
elif symbol == '*':
    small = num1 * num2
elif symbol == '/':
    small = num1 / num2
else:
    print('符号无效.')
print(round(small, 2))
