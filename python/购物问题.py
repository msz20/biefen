thing = input('请输入你要购买的物品：')
price = int (input("请输入你要购买的物品的价格："))
quan = int (input('请输入你要购买的物品的数量：'))
area = price * quan


print(f'您购买的{thing}的总价是{area}美元。')
