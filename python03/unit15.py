for a in range(3, 10):
    print('aaa======aaa', a)

for b in (1, 2, 3, 43):
    print("{} 번".format(a))


aaa = ['1', '2', '3']
bbb = ['2000', '1230', 3000]
print(list(zip(aaa, bbb)))
for (a, b) in zip(aaa, bbb):
    print("{}는 {}원 입니다.".format(a, b))


