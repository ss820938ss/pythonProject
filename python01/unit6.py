# 변수 여러개를 한번에 만들기
x, y = 10, 20
print(x)
print(y)
print()
x, y = y, x
print(x)
print(y)
print("========")

# 변수 삭제하기
x, y = 10, 20
del y
print(x)
# print(y)
print("========")

# 빈 변수 만들기
x = None  # null 과 동일, 대문자 주의
print(x)
print("========")

# 변수로 계산하기
a = 10
b = 20
c = a + b
print(c)
c = a ** b  # 계산식 적용
print(c)
print("========")

# 산술 연산 후 할당 연산자 사용하기
a = 10
a + 20  # 변수 저장이 없어서 결과에 적용 x
print(a)  # 결과 10

# a = a + 20
# print(a) # 결과 30

a += 20  # 위와 같은 식, 뺄샘 나눗셈 등도 동일적용, 식 사이에 공백 x
print(a)  # 결과 30

# d += 10
# print(d) # d의 변수를 먼저 만들지 않아서 오류
print("========")

# 부호 붙이기
x = -10
# +x
# print(x)
x = -x  # 그냥 x = 없이 식만 쓰면 -10만 나옴, 콘솔에서만 바로 사용 가능한듯?
print(x)  # 결과 10
# 양수, 음수 부호는 수학공식과 동일
print("========")

# input 이라 주석처리
# 입력 값을 변수에 저장하기
# input 함수 사용하기
# input() # 입력대기상태, 엔터로 실행, 콘솔
# print("========")

# input 함수의 결과를 변수에 할당하기
# x = input()
# print(x) # x 가 입력한 대로 값이 적용
# print()

# x = input("문자열을 입력하세요: ")
# print(x) # x를 입력하면 출력
# print()
# print("========")

# 두 숫자의 합 구하기
# x = input("x >>>")
# y = input("y >>>")
# print(x + y)
# 문자열로 적용
# print()

# x = int(input("x >>>"))
# y = int(input("y >>>"))
# print(x + y)
# int 를 앞에 붙이고 input 을 쓰면 숫자로 적용
# print("========")

# 입력값을 변수 두 개에 저장하기
# x, y = input("x, y >>>").split("##")
# print(int(x) + int(y)) # int 를 떼면 문자로 인식
# .split() << 괄호안에 넣은 문자를 필수로 넣어야 적용
# print("========")

# map 을 사용하여 정수로 변환하기
# x, y = map(int, input("x, y >>>").split(':'))
# print(x + y)  # 입력방식 10:20, 결과 30

# float test
# a, b = map(float, input("a, b >>>").split('-'))
# print(a + b)
# print("========")

