username = (input('请输入你的用户名称:'))
usernames = len(username)
if usernames > 18:
    print('用户名不得超过12个字符.')
elif ' ' in username:
    print('用户名不能有空格.')
elif not username.isalpha():
    print('用户名不能有数字.')
else:
    print(f'欢迎! {username}!')
