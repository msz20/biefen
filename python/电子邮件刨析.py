email = 'msz20110214@outlook.com'
first = email.index('@')
first_in = email[:first]
print(f'前面的内容是{first_in}.')
second_in = email[(first + 1):]
print(f'后面的内容是{second_in}.')