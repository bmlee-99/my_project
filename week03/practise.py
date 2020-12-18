import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

rank_table = soup.select('#regularTeamRecordList_table > tr')
print(rank_table)

for rank_info in rank_table:
    rank = rank_info.select_one("#regularTeamRecordList_table > tr:nth-child(1) > th")
    