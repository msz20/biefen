# print('自己没事做着玩的,有很多bug,有限制\n 1.x必须在最前面\n 2.不能在右边在写一个x')
# equation = input('请输入方程:')
# x = equation.index('x')
# x1 = equation[:x]
# if x1 == '':
#    x1 = 1
# result1 = equation.index('=')
# result = equation[result1]
# symbol = ''
# add = equation.index('+')
# if not add:
#    add = ''
# reduce = equation.index('-')
# if reduce == 0:
#    reduce = ''
# take = equation.index('*')
# if take == 0:
#    take = ''
# remove = equation.index('/')
# if remove == 0:
#    remove = ''
# if add == '+':
#    symbol = '+'
# elif reduce == '-':
#    symbol = '-'
# elif take == '*':
#    symbol = '*'
# elif remove == '/':
#    symbol = '/'
# num = equation.index('+') or equation.index('-') or equation.index('*') or equation.index('/')
# Num = equation[:'='] and equation[num:]
# if symbol == '+':
#    result -= Num
#    result /= x1
#    print(result)
# elif symbol == '-':
#    result += Num
#    print(result)
# elif symbol == '*':
#    result3 = x1 * Num
#    result /= result3
#    print(result)
# elif symbol == '/':
#    result3 = x1 * Num
#    result5 = x1 * result
#     = result3 / result5
#    print(result)
# else:
#    print('未知错误.')
# 其实上面的代码不能跑,我还没有想出判断符号的方法.
# 上面就是我写的屎山python,下面是Chatgpt写的,不得不说人工智能是真的强.
x = float
equation = input("请输入方程:")

# Split the equation into parts
parts = equation.split("=")
left_side = parts[0].strip()
right_side = parts[1].strip()

# Isolate the coefficient of x
coefficient_of_x = float(left_side.split("x")[0] or 1)  # Handle cases with or without a coefficient

# Isolate the constant term on the right side
constant_term = float(right_side)

# Solve for x using the appropriate mathematical operation
if "+" in equation:
    x = (constant_term - coefficient_of_x) / coefficient_of_x
elif "-" in equation:
    x = (constant_term + coefficient_of_x) / coefficient_of_x
elif "*" in equation:
    x = constant_term / (coefficient_of_x * coefficient_of_x)
elif "/" in equation:
    x = coefficient_of_x * constant_term / (coefficient_of_x - coefficient_of_x * constant_term)
else:
    print("未知错误.")

print("x =", x)