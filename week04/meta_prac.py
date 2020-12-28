import requests
# 에이젝스와 같음 (통신)
from bs4 import BeautifulSoup
# 스크레핑에 필요한 두가지친구

url = 'https://platum.kr/archives/120958'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)
# header 에는 내 브라우져는 무엇입니다 라는 것을 알려줌

soup = BeautifulSoup(data.text, 'html.parser')

# 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.
image = soup.select_one('meta[property="og:image"]')['content']
title = soup.select_one('meta[property="og:title"]')['content']
description = soup.select_one('meta[property="og:description"]')['content']
# 스크랩핑 코드이다/ 그대로 복사해서 flask 위에 올리면 된다ㅌ
# 첫번쨰것만 가지고 오는 select_one/CSS selector 문법중 하나이다/안에선 단따옴표 쌍따옴표를 구분해서 쓴다
print(image, title, description)
