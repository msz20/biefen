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
    print('你所输入的的内容无效.')
# 有一个bug,这个文件在执行完white后,在输入人名,就不会执行if语句,会直接印出内容.
# 修好了,花了我20分钟时间.
# 下面是第一次的代码写的跟坨屎似的.
# massage = input('请输入人名:')
# if massage == 'mashuoze':
#   print('说真的,我不知道自己是怎么想的,要写这鬼东西.')
# elif massage == '王丽格':
#   print('妈,你好吗?我不好.')
# elif massage == '王克伟':
#   print('Hello! What fuck?')
# while massage ='':
#    print('请输入您的名字')