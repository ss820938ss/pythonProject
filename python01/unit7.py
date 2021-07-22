# 값을 여러 개 출력하기
print(1, 2, 3)
print(1)
print(2)
print(3)
print('hello', 'python')
print()

a = 10
b = 'hello world'
c = 53.4342
d = '히히히'
# e, f = map(float, input("실수 입력 :").split())
print(a, b, c, b)
# print(e, f)
print("========")

# sep 로 값 사이에 문자 넣기
print(1, 2, 3, sep=', ')  # 값 사이에 해당 문자 넣어줌
print('hello', 'world', sep='===')
print('숫자를 곱해보자 : ', 19329, 32939, sep='x')  # 숫자가 들어갔지만 문자로 적용
print("========")

# 줄바꿈 활용하기
# \n  >>  new line
# \r, \t, \b 등등 있음
print(1, 2, 3, sep='\n')
print('모니터 해상도 : ', 1920, 1080, sep='\t')
print('aaaa\nbbbbb\nccccc\n')
print('하하하 \\ 10,000 안녕.')  # \를 하나만 입력하면 출력이 안됨 2개 필요
print('라라라 \"ㅇㄴㄹㅇㄴ\" fdsfdsf 안녕')
print("========")

# end 사용하기
print(1, end='')
print(2, end='')
print(3)  # end 에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
print()

print("aaa", end='')
print("bbb", end='\n')
print("ccc")
print()

print(1, end=' ')
print(2, end=' ')
print(3)
print("========")
print()

# 연습문제 : 날짜와 시간 출력
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59
print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')
print("========")

# 예제 2
year = 1999
month = 12
day = 31
hour = 10
minute = 37
second = 21
print(year, month, day, sep='-', end='')
print("T", end='')
print(hour, minute, second, sep=':')
print("========")

# 예제 3
# 2017 10 27 11 43 59
year, month, day, hour, minute, second = input("날짜를 입력하세요 >").split(" ")
print(year, month, day, sep='-', end='')
print('T', end='')
print(hour, minute, second, sep=':')
