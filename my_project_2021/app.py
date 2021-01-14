from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)


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
        'display': '50',
        'start': '1',
        'sort': 'sim',
    }
    response = requests.get('https://openapi.naver.com/v1/search/news.json', headers=headers, params=params)
    data = response.json()
    print(data)
    return jsonify({'result': 'success', 'data': data})


@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
