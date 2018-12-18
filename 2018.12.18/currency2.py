import requests
from bs4 import BeautifulSoup

req = requests.get("https://academic.naver.com/").text
soup = BeautifulSoup(req, 'html.parser')

scholar = soup.select_one("#search_type_text")
print(scholar.text)

# 네이버 실시간 검색어 스크래핑

