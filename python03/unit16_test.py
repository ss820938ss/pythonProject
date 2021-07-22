# 연습 1
print("=====가격표=====")
coffee = ['아메리카노', '카페라떼', '콜드브루', '콜드브루라떼', '돌체라떼']
price = ['2000', '3000', '3500', '4000', '4500']
print(list(zip(coffee, price)))
for (x, y) in zip(coffee, price):
    print("{}는 {}원 입니다.".format(x, y))
print()

# 연습 2
print('=====커피 주문=====')
menu = {'1. 아메리카노': 2000, '2. 카페라떼': 3000, '3. 콜드브루': 3500, '4. 콜드브루라떼': 4000, '5. 돌체라떼': 4500}
print(menu)
print('메뉴의 번호를 선택해 주세요.')
order = int(input())
if order == 1:
    print('아메리카노 2000원 입니다.')
elif order == 2:
    print('카페라떼 3000원 입니다.')
elif order == 3:
    print('콜드브루 3500원 입니다.')
elif order == 4:
    print('콜드브루라떼 4000원 입니다.')
else:
    print('돌체라떼 4500원 입니다.')
