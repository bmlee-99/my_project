from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/my_page')
# # 함수이름 중복 no
# def my_page():
#     return 'Hello My Page!'

@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')

    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})
# json 형태로 응답이 온다

@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
