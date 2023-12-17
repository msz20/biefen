massage = input('请输入人名:')
while massage == '':
    massage = (input('请输入人名:'))
if massage == 'mashuoze':
    print('说真的,我不知道自己是怎么想的,要写这鬼东西.')
elif massage == '王丽格':
    print('妈,你好吗?我不好.')
elif massage == '王克伟':
    print('Hello! What fuck?')
else:
    print('无效')
# 有一个bug,这个文件在执行完white后,在输入人名,就不会执行if语句,会直接印出内容.
# 修好了.