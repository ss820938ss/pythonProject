# 딕셔너리 사용하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux)

# 딕셔너리에 키와 값을 저장할 때 키가 중복되면 가장 뒤에 있는 값만 사용
lux2 = {'health': 800, 'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux2['health'])
print(lux2)
print("========")

# 딕셔너리 키의 자료형
# 딕셔너리의 키는 문자열뿐만 아니라 정수, 실수, 불도 사용할 수 있으며 자료형을 섞어서 사용해도 됨
# 값에는 리스트, 딕셔너리 등을 포함하여 모든 자료형을 사용할 수 있음
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
print(x)

# 키에는 리스트와 딕셔너리를 사용할 수 없음
# y = {[10, 20]: 100}
# print(y)  # 오류
print("========")

# 빈 딕셔너리 만들기
z = {}
print(z)

# 예시 2
a = dict()
print(a)
print("========")

# dict 로 딕셔너리 만들기
# 키에 ' '(작은따옴표)나 " "(큰따옴표)를 사용하지 않아야 함
lux3 = dict(health=490, mana=334, melee=550, armor=18.72)
print(lux3)

# 두 번째 방법은 dict 에서 zip 함수를 이용하는 방법
# 키가 들어있는 리스트와 값이 들어있는 리스트를 차례대로 zip 에 넣은 뒤 다시 dict 에 넣어주면 됨
lux4 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
print(lux4)

# 세 번째 방법은 리스트 안에 (키, 값) 형식의 튜플을 나열하는 방법
lux5 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux5)

# 네 번째 방법은 dict 안에서 중괄호로 딕셔너리를 생성하는 방법
lux6 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
print(lux6)
print("========")

# 딕셔너리의 키에 접근하고 값 할당하기
# 딕셔너리의 키에 접근할 때는 딕셔너리 뒤에 [ ](대괄호)를 사용하며 [ ] 안에 키를 지정해주면 됨
lux7 = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux7['health'])

# 딕셔너리는 [ ]로 키에 접근한 뒤 값을 할당함
lux8 = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux8['health'] = 2037
lux8['mana'] = 1184
print(lux8)

# 딕셔너리에 없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당됨
lux8['mana_regen'] = 3.28
print(lux8)

# 딕셔너리에 없는 키에서 값을 가져오려고 하면 에러가 발생함
# print(lux8['attack_speed'])  # 오류
print("========")

# 딕셔너리에 키가 있는지 확인하기
# 딕셔너리에서 키가 있는지 확인하고 싶다면 in 연산자를 사용하면 됨
print('health' in lux)
print('attack_speed' in lux)

# 반대로 in 앞에 not 을 붙이면 특정 키가 없는지 확인함
print('attack_speed' not in lux)
print('health' not in lux)

# 키의 개수는 len 함수를 사용하여 구함(키와 값은 1:1 관계이므로 키의 개수는 곧 값의 개수임)
print(len(lux))
# len(lux)와 같이 len 에 딕셔너리 변수를 넣어서 키의 개수를 구해도 되고, len 에 딕셔너리를 그대로 넣어도 됨
