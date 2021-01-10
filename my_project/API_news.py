import requests


headers = {
    'X-Naver-Client-Id': 'GB58KoYEkcQOWJawE0MA',
    'X-Naver-Client-Secret': 'p1TNjrjmzL',
}

params = {
    'query': 'erp',
    'display': '10',
    'start': '1',
    'sort': 'sim',
}


response = requests.get('https://openapi.naver.com/v1/search/news.json', headers=headers, params=params)
data = response.json()
print(data)