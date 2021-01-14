import requests
from flask import Flask
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.dbsparta
headers = {
    'X-Naver-Client-Id': 'GB58KoYEkcQOWJawE0MA',
    'X-Naver-Client-Secret': 'p1TNjrjmzL',
}

params = {
    'query': 'erp',
    'display': '20',
    'start': '1',
    'sort': 'sim',
}


response = requests.get('https://openapi.naver.com/v1/search/news.json', headers=headers, params=params)
data = response.json()
print(data)

@app.route('/api/newslist', methods=['GET'])
def news_list():
    # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    news_list = list(db.mystar.find({}, {'_id': False}).sort('like', -1))
    # sort() 정열하겠다 -1 내림차순->몽고DB 의 기능

    return jsonify({'result': 'success', 'data': news_list })


