import requests as rq#크롤링
from bs4 import BeautifulSoup#파서

def get_html(url):
    _html = ""
    resp = rq.get(url)
    if resp.status_code == 200:
      _html = resp.text
    return _html
# r = rq.get('https://www.naver.com/', auth=('user','pass'))
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.text)
# print(r.json)
# requests 모듈 사용법


target_URL = "https://www.naver.com/"
target_html = get_html(target_URL)
soup = BeautifulSoup(target_html,'html.parser')
num = soup.find_all("li")
print(len(num))