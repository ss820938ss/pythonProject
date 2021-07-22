import requests

# 1
print('hello world')
# 2
print("Mary's cosmetics")
# 3
print('신씨가 소리질렀다. "도둑이야".')
# 4
print("C:\Windows")
# 5
print("안녕하세요.\n만나서\t\t반갑습니다.")
#  \n 은 줄바꿈 \t는 탭간격주기
# 6
print("오늘은", "일요일")
# 7
print('naver', 'kakao', 'sk', 'samsung', sep=';')
# 8
print('naver', 'kakao', 'sk', 'samsung', sep='/')
# 9
print('print("first")', 'print("second")', sep=';')
# 10
print(5 / 3)

btc = requests.get("http://api.bithumb.com/public/ticker/").json()['data']



