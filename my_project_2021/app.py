from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup

app = Flask(__name__)
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost, 27017)')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('my_project_html.html')


@app.route('/search', methods=['GET'])
def test_get():
    keyword_receive = request.args.get('keyword_give')
    headers = {
        'X-Naver-Client-Id': 'GB58KoYEkcQOWJawE0MA',
        'X-Naver-Client-Secret': 'p1TNjrjmzL',
    }
    params = {
        'query': keyword_receive,
        'display': '20',
        'start': '1',
        'sort': 'sim',
    }
    response = requests.get('https://openapi.naver.com/v1/search/news.json', headers=headers, params=params)
    data = response.json()
    print(data)
    return jsonify({'result': 'success', 'data': data})


def insert_image():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/73.0.3683.86 Safari/537.36'}
    from my_project_2021.API_news import params
    data = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum', headers=headers, params=params)

    soup = BeautifulSoup(data.text, 'html.parser')

    image = soup.select_one('#main_pack > section.sc_new sp_nnews _prs_nws > div.api_subject_bx > div.group_news > '
                            'div.news_wrap api_ani_send > a > img').text

    doc = {
        'image': image,
    }

    db.mystar.insert_one(doc)
    # mystar 라고 생성함
    print('완료!')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
