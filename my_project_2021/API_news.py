import requests
from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML 화면 보여주기
@app.route('/')
def my_project():
    return render_template('index.html')

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


