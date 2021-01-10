from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


# hmtl 를 응답해준다 -> 서버 쪽 이구나/index.html은 클라이언트 쪽이다


@app.route('/memo', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기/키가 정확히 ajax 에서의 키와 일치해야한다
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    # 브라우저에서 데이터를 집어넣고 버튼을 누르면 서버에서 통신을 받아 그 정보가 떠야한다
    #     print(url_receive,comment_receive)
    # 2. meta tag를 스크래핑하기
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    image = soup.select_one('meta[property="og:image"]')['content']
    title = soup.select_one('meta[property="og:title"]')['content']
    description = soup.select_one('meta[property="og:description"]')['content']
                # print(image, title, description)

    # 3. mongoDB에 데이터 넣기
    doc = {
        'url':url_receive,
        'comment':comment_receive,
        'title':title,
        'image':image,
        'description':description

    }


    db.articles.insert_one(doc)


    return jsonify({'result': 'success', 'msg': '작성 완료!'})


@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    article_list = list(db.articles.find({},{'_id':False}))
    # {'_id': False} 안가지고 오겠다는 뜻, json 형식이 아니기 때문
    # print(article_list)
    # 브라우져에 http: // localhost: 5000 / memo 로 적엇 확인할수 있음


    # 2. articles라는 키 값으로 articles 정보 보내주기
    return jsonify({'result': 'success', 'data': article_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)