# 비교 연산자의 판단 결과
print(3 > 1)
print("========")

# 숫자가 같은지 다른지 비교하기
print(10 == 10)  # 10과 10이 같은지 비교
print(10 != 5)  # 10과 5가 다른지 비교
# 숫자만이 아니라 문자열도 비교가능
print("========")

# id 함수
# 정수 객체와 실수 객체가 서로 다른지 확인하려면 id 함수를 사용하면 됨
# id는 객체의 고유한 값(메모리 주소)을 구함(이 값은 파이썬을 실행하는 동안에는 계속 유지되며 다시 실행하면 달라짐)
print(id(1))
print(id(1.0))
# 두 객체의 고유한 값이 다르므로 서로 다른 객체임
print("========")

# 정수, 실수, 문자열을 불로 만들기
print(bool(1))
print(bool(0))
print(bool(1.5))
print(bool('False'))
# 정수 0, 실수 0.0이외의 모든 숫자는 True임
# 빈 문자열 '', ""를 제외한 모든 문자열은 True임
print("========")

# 단락 평가
# and 연산자는 두 값이 모두 참이라야 참이므로 첫 번째 값이 거짓이면 두 번째 값은 확인하지 않고 바로 거짓으로 결정함
print(False and True)
print(False and False)
# or 연산자는 두 값 중 하나만 참이라도 참이므로 첫 번째 값이 참이면 두 번째 값은 확인하지 않고 바로 참으로 결정함
print(True or False)
print(True or False)
print("========")

# 문자열 'Python' 도 불로 따지면 True 라서 True and True 가 되어 True 가 나올 것 같지만 'Python' 이 나옴
# 파이썬에서 논리 연산자는 마지막으로 단락 평가를 실시한 값을 그대로 반환하기 때문임
print(True and 'Python')
# 논리 연산자는 무조건 불을 반환하지 않음
# 다음과 같이 마지막으로 단락 평가를 실시한 값이 불이면 불을 반환하게 됨
print('Python' and True)
print('Python' and False)
print("========")

# 문자열 'Python' 을 True 로 쳐서 and 연산자가 두 번째 값까지 확인하므로 두 번째 값이 반환됨
print(False and 'Python')
# and 연산자 앞에 False 나 False 로 치는 값이 와서 첫 번째 값 만으로 결과가 결정나는 경우에는 첫 번째 값이 반환됨
print(0 and 'Python')
# or 연산자도 마찬가지로 마지막으로 단락 평가를 실시한 값이 반환됨
print(True or 'Python')
# or 연산자에서 첫 번째 값만으로 결과가 결정되므로 첫 번째 값이 반환됨
print('Python' or True)
# 두 번째 값까지 판단해야 한다면 두 번째 값이 반환됨
print(False or 'Python')
print(0 or False)
print("========")
print()

# 연습문제 : 합격 여부 출력하기
korean = 92
english = 47
mathematics = 86
science = 81
print(korean >= 50 and english >= 50 and mathematics >= 50 and science >= 50)
print("========")

# 심사문제 : 합격 여부 출력하기
korean = 90
english = 81
mathematics = 86
science = 80
print(korean >= 90 and english > 80 and mathematics > 85 and science >= 80)
print("========")

korean = 90
english = 80
mathematics = 85
science = 80
print(korean >= 90 and english > 80 and mathematics > 85 and science >= 80)