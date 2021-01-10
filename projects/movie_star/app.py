from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_stars():
    # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    star_list = list(db.mystar.find({}, {'_id': False}).sort('like', -1))
    # sort() 정열하겠다 -1 내림차순->몽고DB 의 기능

    return jsonify({'result': 'success', 'data': star_list})


@app.route('/api/like', methods=['POST'])
def like_star():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    name_receive = request.form['name_give']
    db.mystar.update_one({'name': name_receive}, {'$inc': {'like': 1}})
    # 1씩 증가시킨다는 뜻 inc 라는 업데이트 오퍼레이터

    # # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    # star = db.mystar.find_one({'name': name_receive})
    #
    # # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    # new_like = star['like'] + 1
    #
    # # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    # # 참고: '$set' 활용하기! update 하기
    # db.mystar.update_one({'name': name_receive}, {'$set': {'like':new_like}})
    # # 마이스타에서 한명을 업뎃-> 전달받은 이름을 변경-> 기존에 있는걸 바꾸겠다

    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg': '좋아요!'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_give']

    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
    db.mystar.delete_one({'name': name_receive})
    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg': '삭제 되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
