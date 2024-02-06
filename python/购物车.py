Menu = {
    "披萨" : 100,
    "可乐" : 60,
    "爆米花" :70,
    "薯条" : 90,
}
cart = []
Total = 0
print('菜单')
print('------------------')
for item, price in Menu.items():
    print(f"{item}: {price}")
while True:
    food = input("请输入种类（按Q结束）")
    if food == 'Q':
      break
    elif Menu.get(food) is None:
       print('菜单中无此商品。')
    else:
       cart.append(food)
       Total = Menu.get(food)
print(f'总共为{Total}元')