import json
import pickle as pi

# # 테스트용 Python Dictionary
# customer = {
#     'id': 152352,
#     'name': '강진수',
#     'history': [
#         {'date': '2015-03-11', 'item': 'iPhone'},
#         {'date': '2016-02-23', 'item': 'Monitor'},
#     ]
# }
#
# # JSON 인코딩
# jsonString = json.dumps(customer)
#
# # 문자열 출력
# print(jsonString)
# print(type(jsonString))  # class str
# print()
#
# # 테스트용 JSON 문자열
# jsonString = '{"name": "강진수", ' \
#              '"id": 152352, ' \
#              '"history": [' \
#              '{"date": "2015-03-11", "item": "iPhone"}, ' \
#              '{"date": "2016-02-23", "item": "Monitor"}]}'
#
# # JSON 디코딩
# dict = json.loads(jsonString)
#
# # Dictionary 데이타 체크
# print(dict['name'])
# for h in dict['history']:
#     print(h['date'], h['item'])
# print()
#
# customer = {
#     'id': 152352,
#     'name': '강진수',
#     'history': [
#         {'date': '2015-03-11', 'item': 'iPhone'},
#         {'date': '2016-02-23', 'item': 'Monitor'},
#     ]
# }

#
# jsonString = json.dumps((customer))
#
# file = open("../test2.txt", 'a')
# file.write(jsonString)
# file.close()


name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
with open('james.p', 'wb') as file:
    pi.dump(name, file)
    pi.dump(age, file)
    pi.dump(address, file)
    pi.dump(scores, file)
print()

with open('james.p', 'rb') as file:
    name = pi.load(file)
    age = pi.load(file)
    address = pi.load(file)
    scores = pi.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)