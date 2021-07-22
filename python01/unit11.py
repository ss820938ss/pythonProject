# 시퀀스 자료형 활용하기
a = list(range(0, 100, 10))
print(a)

# a 안에 해당 숫자가 있는지
print(30 in a)
print(100 in a)

# a 안에 해당 숫자가 없는지
print(100 not in a)
print(30 not in a)
print("========")

# 특정 값이 있는지 확인하기
print(43 in (38, 76, 43, 62, 19))
print(1 in range(10))
print('P' in 'Hello, Python')
print("========")

# 시퀀스 객체 연결하기
x = list(range(0, 40, 10))
y = [9, 8, 7, 6]
print(x + y)
print("========")

# 시퀀스 자료형 중에서 range 는 + 연산자로 객체를 연결할 수 없음
# print(range(0, 10) + range(10, 20))  # 오류
# range 를 리스트 또는 튜플로 만들어서 연결하면 됨
print(list(range(0, 10)) + list(range(10, 20)))  # 리스트
print(tuple(range(0, 10)) + tuple(range(10, 20)))  # 튜플
# 문자열은 + 연산자로 여러 문자열을 연결 가능
print('hello!,' + 'world!')
print("========")

# 시퀀스 객제 반복하기
print([0, 10, 20, 30] * 3)
# 0 또는 음수를 곱하면 빈 객체가 나오며 실수는 곱할 수 없음

# 전달매개변수 = parameter
# range 는 연산자로 객체를 연결 불가, 리스트나 튜플로 변환 후 가능
print(list(range(0, 13, 2)) * 3)
print(tuple(range(0, 8, 3)) * 3)
print("========")

# 시퀀스 객체의 요소 개수 구하기
# 리스트와 튜플의 요소 개수 구하기
b = [10, 23, 232, 44, 5]
print(len(b))
c = (23, 34, 232, 449, 994)
print(len(c))
print("========")

# range 의 숫자 생성 개수 구하기
print(len(range(0, 10, 2)))
print()

# 문자열의 길이 구하기
d = 'dissuaded'
e = '가나다라마바사'
print(len(d))
print(len(e))
# 사용하는 글자 갯수 구해주지만 용량은 다름
print("========")

# 인덱스 사용하기
# 인덱스는 0부터 시작
aa = [304, 34, 23, 45, 593]
print(aa[1])
print(aa[0])
print(aa[4] - 1)  # 해당 숫자에서 -1로 출력
print(aa[4] - aa[1])  # 해당 리스트 안의 숫자끼리 값을 -해서 출력
print()

# 튜플
bb = (394, 22, 34, 99, 39)
print(bb[3])
print(bb[0])


# 문자형도 꺼내기 가능
# 음수 인덱스도 지정 가능 (단 0이 아닌 1부터 시작)
print(bb[-2])

# 마지막 요소에 접근하기
print(bb[len(bb) - 1])  # 갯수인 5로 나오면 인덱스 범위를 벗어나므로 -1을 해줘야 됨
print("========")

# 요소에 값 할당하기
cc = [0, 0, 0, 0, 0]
print(cc)
cc[0] = 34
cc[1] = 23
cc[2] = 12
cc[3] = 50
cc[4] = 98
print(cc)
print(cc[1])
print(cc[0])
# 시퀀스 자료형 중에서 튜플, range, 문자열은 읽기 전용임
print("========")

# del 로 시퀀스 객체의 요소를 삭제해보자
dd = [49, 69, 309, 30, 61]
del dd[2]
print(dd)
print()

# 리스트와는 달리 튜플은 요소를 삭제할 수 없음
# 마찬가지로 range 와 문자열도 안에 저장된 요소를 삭제할 수 없음
ee = (394, 33, 92, 4, 12)
# del ee
print(ee)  # 튜플 전체는 삭제가능
f = [394, 33, 92, 4, 12]
print(id(ee))
print(id(f))  # 숫자는 같아도 둘은 서로 다른 데이터
print("========")

# 슬라이스 사용하기
g = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(g[0:4])  # 리스트의 일부를 잘라서 새 리스트를 만듦

h = [20, 30, 40, 50]
print(h[:])  # 범위 생략시 시작부터 끝까지

# 예를 들어 요소가 10개 들어있는 리스트를 처음부터 끝까지 가져오려면 [0:9]가 아닌 [0:10]이라야 함
# (끝 인덱스는 범위를 벗어난 인덱스를 지정할 수 있음)
print(g[0:10])

# a[1:1]처럼 시작 인덱스와 끝 인덱스를 같은 숫자로 지정하면 아무것도 가져오지 않음
print(g[1:1])  # 에러는 나지 않음

# a[1:2]처럼 끝 인덱스에 1을 더 크게 지정해야 요소 하나를 가져옴
print(g[1:2])

#  리스트의 중간 부분 가져오기
print(g[4:-1])

# 인덱스 증가폭 사용하기
# 슬라이스는 인덱스의 증가폭을 지정하여 범위 내에서 인덱스를 건너뛰며 요소를 가져올 수 있음
print(g[2:8:3])  # 인덱스 2를 +3 해서 7까지 가져옴
# 인덱스 증가폭을 지정하더라도 가져오려는 인덱스(끝 인덱스 - 1)를 넘어설 수 없다는 점을 꼭 기억해두자
# 끝 인덱스 - 1과 증가한 인덱스가 일치한다면 해당 요소까지 가져올 수 있음

# 인덱스 생략하기
print(g[:7])
# 시작 인덱스를 생략하면 리스트의 처음부터 끝 인덱스 - 1(인덱스 6)까지 가져옴

# 끝 인덱스를 생략하면 시작 인덱스(인덱스 7)부터 마지막 요소까지 가져옴
print(g[7:])
print("========")

# 인덱스를 생략하면서 증가폭 사용하기
print(g[7::2])
print(g[::2])
print(g[::])
print()

# len 응용하기
print(g[0:len(g)])
print(g[:len(g)])
# 결과 동일
print("========")

# 튜플에 슬라이스 사용하기
ff = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(ff[2:6]) #  파이썬에서는 튜플, range, 문자열도 시퀀스 자료형이므로 리스트와 같은 방식으로 슬라이스를 사용할 수 있음
print(ff)
gg = ff[2:6]
print(gg)  # 자른 결과가 출력
print()

# range 에 슬라이스를 사용하면 지정된 범위의 숫자를 생성하는 range 객체를 새로 만듦
hh = range(10)
print(list(hh))
hh = hh[1:5]  # 아래와 결과 동일
# hh = list(hh[1:5])
print(list(hh))  # list 를 붙이지 않으면 일반 range 로 인식
print()

# 슬라이스에 요소 할당하기
i = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
i[2:5] = ['a', 'b', 'c']
print(i)
print()

# 요소 개수를 맞추지 않아도 알아서 할당됨
# 할당할 요소 개수가 적으면 그만큼 리스트의 요소 개수도 줄어듦
l = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
l[2:5] = ['a']
print(l)
print()

# m[2:8:2] = ['a', 'b', 'c']와 같이 인덱스 2부터 2씩 증가시키면서 7까지 'a', 'b', 'c'를 할당함
m = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
m[2:8:2] = ['a', 'b', 'c']  # 간격(마지막 숫자) 을 지우고 실행할 경우 앞 간격만큼 문자열 대체(나머지 번호 잘림)
print(m)
# 갯수와 요소가 맞지 않을 경우 오류
print("========")

# 10을 생성 > 리스트 j 를 k 로 전환 > k 의 0번 인덱스를 10으로 변환 > 출력
j = range(10)
k = (list(j))
k[0] = 10
print(k)
print()

# 응용 1
# ii 리스트에 담기 > jj 로 넣기 > 출력 > kk 에 문자 넣기 > jj 9번 인덱스에 kk 넣기 > jj 출력 > jj 2번 인덱스에 새 숫자 리스트 넣기
# = 최종결과 : [10, 20, 30, 2, 3, 4, 5, 6, 7, 8, ['di', 'rg']]
ii = range(10)
print(list(ii))
jj = (list(ii))
print(jj)
kk = ['di', 'rg']
jj[9] = kk
print(jj)
jj[:2] = [10, 20, 30]
print(jj)
print()

# 응용 2
# aaa range 로 10까지 생성 > 리스트 출력 > bbb 에 aaa 담기 > bbb 출력 > ccc ddd 문자 리스트 생성
# > 1) bbb 의 앞에서부터 2번째까지 담기 > 출력
# > 최종결과 : [['df', 'dfe'], ['gi', 'hello'], 2, 3, 4, 5, 6, 7, 8, 9]
# > 2) bbb 의 뒤에섯부터 2번째에 중복해서 3회 담기(같은 문자 반복) > 출력
# > 최종결과 : [0, 1, 2, 3, 4, 5, 6, 7, 8, ['df', 'dfe'], ['df', 'dfe'], ['df', 'dfe'], 9]
aaa = range(10)
print(list(aaa))
bbb = (list(aaa))
print(bbb)
ccc = ['df', 'dfe']
ddd = ['gi', 'hello']
print(bbb)
bbb[:2] = [ccc, ddd]
# bbb[-1:2] = [ccc, ccc, ccc]
print(bbb)
print()

# 응용 3
# person1, 2, 3 데이터 준비 > addList 에 인덱스 번호 매겨서 담기 > 출력
# > 결과 : (인덱스 번호 붙일시) 해당 번호 자료 출력 ['강감찬', '서울광역시', 21, '010-431-2243']
# > 결과 : (인덱스 번호 붙이지 않을시) 전체 자료 출력
addList = [1, 2, 3]
person1 = ['홍길동', '대구광역시', 25, '010-555-2111']
person2 = ['김유신', '대전광역시', 40, '010-512-3243']
person3 = ['강감찬', '서울광역시', 21, '010-431-2243']

addList[0] = person1
addList[1] = person2
addList[2] = person3
print(addList[2])
print("========")

# del 로 슬라이스 삭제하기
eee = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del eee[2:5]
print(eee)

# 인덱스 2부터 2씩 증가시키면서 인덱스 6까지 삭제함
fff = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del fff[2:8:2]
print(fff)
# 튜플, range, 문자열은 del 로 슬라이스를 삭제할 수 없음

