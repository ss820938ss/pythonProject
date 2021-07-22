# 리스트 만들기
a = [10, 12, 130, 343, 234, 'ddd', 'crge']
print(type(a))
print(a)
print("========")

b = (23, 25, 354, 324)
print(type(b))
print(b)
print("========")

c = [10, 12, 130, 343, 234, 'ddd', 'crge', b]
print(c)
print("========")

# 빈 리스트 만들기
d = []
print(d)
print("========")

# range 를 사용하여 리스트 만들기
print(range(10))
print("========")

aa = list(range(10))
print(aa)
print("========")

bb = list(range(5, 13))
print(bb)
print("========")

cc = list(range(-4, 10, 2))
print(cc)
print("========")

dd = list(range(10, 0, -1))
print(dd)
print("========")
print()

# 튜플 사용하기
e = (1, 3, 4, 53, 55)
print(e)
# 변수 보호를 위해 사용, 변하지 않음
print("========")

f = (34)
print(type(f))  # 요소 한개짜리는 튜플이 아니라 값이 됨

g = (34, )
print(type(g))  # 튜플로 요소하나를 넣을때는 , 공백 사용
print("========")

# range 를 사용하여 튜플 만들기
ee = tuple(range(10))
print(ee)

# 5부터 11까지 들어있는 튜플
ff = tuple(range(5, 12))
print(ff)

# range에 증가폭을 지정하는 방법도 가능함
# range(시작, 끝, 증가폭)
gg = tuple(range(-4, 10, 2))
print(gg)
print("========")

# 튜플 <-> 리스트 바꾸기
h = [1, 3, 4]
print(tuple(h))
print("========")

i = (3, 4, 5)
print(list(i))
print("========")
print()

# 연습문제 : range 로 리스트 만들기
j = list(range(5, -11, -2))
print(j)
print("========")

# 심사문제 : range 로 튜플 만들기
hh = tuple(range(-10, 10, 2))
print(hh)
print()

ii = tuple(range(-10, 10, 3))
print(ii)
print("========")

