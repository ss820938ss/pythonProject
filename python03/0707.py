# import urllib.request
#
# with urllib.request.urlopen('http://www.python.org') as f:
#     print(f.read())
# import hello
#
# def main():
#     print('hello 모듈시작')
#     print('hello.py __name__:', __name__)
#     print('hello 모듈 끝')
#     hello.hello_fun()
#
# if __name__ == '__main__':
#     main()

import requests
from bs4 import BeautifulSoup

response = requests.get("http://pythondojang.bitbucket.io/weather/observation/currentweather.html")


def beautifulSoup(content, param):
    pass

soup = beautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class':'table_develop3'})

data = []
for tr in table.find('tr'):
    tds = list(tr.find_all('td'))

    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temperature = tds[5].text
            humidity = tds[9].text
            data.append([point, temperature, humidity])

            print(td)