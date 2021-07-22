# 여러줄로 된 문자열 사용하기
hello = '''
    hello, ddd!
    안녕하세요.
    python입니다.
    a = 10
            b = 'hello world'
    c = 53.4342
    d = '히히히'
'''
print(hello)  # 쓴 그대로 출력, 다른 식 들어가도 무시하고 글자 취급
print("========")

# 문자열에 따옴표를 포함하는 다른 방법
print('distills r\'daffodils')
# 작은따옴표 앞에 \(역슬래시)를 붙이면 됨
# 큰따옴표도 "He said \"Python is easy\""처럼 큰따옴표 앞에 \를 붙이면 됨
print("========")

# 연습문제 : 여러 줄로 된 문자열 사용하기
s = '''
Python is a programming language that lets you work quickly
and
integrate systems more effectively
'''
print(s)