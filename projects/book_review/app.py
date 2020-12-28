# 서버이다

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 응답해주는 코드주는 부분->route로 get 방식으로 왔을때 html 응답
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    # 1. 클라이언트가 준 title, author, review 가져오기.
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    # 2. DB에 정보 삽입하기
    doc = {
        'title': title_receive,
        'author': author_receive,
        'review': review_receive
    }
    db.reviews.insert_one(doc)
    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '작성완료'})


@app.route('/review', methods=['GET'])
# get방식은 브라우져에서 볼수 있으
def read_reviews():
    review_list = list(db.reviews.find({},{'_id':False}))
    # print(review_list)
    # curserr를 없애는 방법은 list 로 감싼다_커서는 위치만 알려줌
    # objectId는 json 형식으로 받아들어지지않음
    return jsonify({'result': 'success', 'data': review_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
