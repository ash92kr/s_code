import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

# 개별적인 id로 .PM_CL_realtimeKeyword_rolling을 선택
# >는 바로 아래의 자식이라는 뜻이고 >가 없으면 모든 자식을 의미한다
for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):  
    rank = tag.select_one('.ah_r').text   # 태그 대신 숫자만 뽑기
    keyword = tag.select_one('.ah_k').text
    print(f'{rank}위의 검색어는 {keyword}입니다.')
    # print((tag.select_one('.ah_r)).text)

# 전체 단어
datas = soup.select("#PM_ID_ct > div > div > div > div > div > ul > li > a > span")

ranks = soup.select('#PM_ID_ct > div > div > div > div > div > ul > li > a > span.ah_r')
keywords = soup.select('#PM_ID_ct > div > div > div > div > div > ul > li > a > span.ah_k')

for i in range(len(ranks)):
    print(ranks[i].text + "위 " + keywords[i].text)

