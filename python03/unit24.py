# 문자열 서식 지정자와 포매팅 사용하기
print('I am %s' % 'james')
name = 'maria'
print('I am %s' % name)
print()

# name = '최영민'
# name2 = input("별명을 입력하세요 :")
# print('나의 이름은 %s 이고 별명은 %s 입니다.' % (name, name2))
# 입력 > 우우우, 결과 > 나의 이름은 최영민 이고 별명은 (입력:우우우) 입니다.
# print()

print('i am %d years old.' % 20)
print()

# 지정 서식자로 소숫점 표시하기
print('%f' % 3.5)
print('%.3f' % 3.2)  # 소숫점 이하 길이 지정
print()

# 서식 지정자로 문자열 정렬하기
print('%10s' % 'python')  # %10s 10칸 생성후 글자를 넣고 빈자리는 앞쪽에 공백
name = '최영민'
print('%-10s' % (name))  # -를 쓰면 문자 뒤에서부터 공백
print()

# 서식 지정자로 문자열 안에 값 여러 개 넣기
print('Today is %d %s.' % (3, 'April'))
# % (3,'April') 로 쓰면 결과도 붙어나옴
print()
print("========")

# format 메서드 사용하기
print('hi, {0}'.format('world!'))
print('ddd {0}'.format(222))
print()

# format 메서드로 값을 여러 개 넣기
print('hi, {0} {2} {1}'.format('Python', 'Script', 3.6))

# format 메서드로 같은 값을 여러 개 넣기
print('{0} {0} {1} {1}'.format('hi', 'Python'))  # 인덱스 번호따라 반복됨

# format 메서드에서 인덱스 생략하기
print('hello, {} {} {}'.format('hi', 'python', 3.7))  # 인덱스 번호지정이 없으면 포맷 순서대로 값이 들어감

# format 메서드에서 인덱스 대신 이름 지정하기
print('Jeju, {language} {version}'.format(language='Python', version=3.7))  # {} 에 인덱스 대신 이름 지정
print()

# 문자열 포매팅에 변수를 그대로 사용하기
language = 'Jeju'
version = 3.8
# print(f'Hello, {language} {version}')
print(f'hello, {language} {version}'.format(language='python', version=3.3))  # 이미 위에 지정되었기 때문에 변함 x
