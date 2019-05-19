import requests
from bs4 import BeautifulSoup

url = 'http://www.op.gg/summoner/userName='
username = 'hide on bush'   # 대소문자 상관없음

response = requests.get(url+username).text
soup = BeautifulSoup(response, 'html.parser')
wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')

print(wins.text)   # 이긴 횟수
print(loses.text)   # 진 횟수


