import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 크롬 브라우져에서 요청한다고 브라우져 정보를 추가로 넣는것/ 유저 에이전트가 없으면 서버에서 응답을 안해주는 경우가 있음/사실 밑에만 있으도 됨
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# 파이션에서 html 를 분석한 정보가 뽑아짐
trs = soup.select("#old_content > table > tbody > tr")
# > 직계후손이라는 뜻/ tr(2) 는 두번째 tr 를 가지고 오라는 뜻/마우스 오른쪽의 copy selector(css selector)를 가지고 옴
# select_one 는 하나를 select 는 전체를 가지고 오는것: tr안에 이름이 있다고 전략을 세움/ 이미 tr: table row 을 반복문을 돌고 있음
for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    if a_tag != None:
        name = a_tag.text
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        print(rank, name)
        point = tr.select_one('td.point').text
        # tr 밑에 있기 때문에, 평점은 하나밖에 없음
        print(rank, name, point)
        doc = {
            'rank': rank,
            'title': name,
            'star': point  # DB에는 숫자처럼 생긴 문자열 형태로 저장됩니다.
        }
        db.movies.insert_one(doc)
