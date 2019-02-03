import requests
import csv
import datetime
import json
from pprint import pprint
import os

def csv_writes(file_name, list1, list2, list3, list4):
    
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ('movie_code', 'title', 'audience', 'recorded_at')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(len(list1)):
            writer.writerow({'movie_code': list1[i], 'title': list2[i], 'audience': list3[i], 'recorded_at': list4[i]})

movieCode = []   # 영화 대표코드
movieName = []   # 영화명
watchAccount = []   # 해당일 누적관객수
countDay = []   # 해당일

for i in range(10):
    key = os.getenv("key_bot")
# 본인의 개인키
    latest = datetime.date(2019, 1, 13)
    targetDt = (latest - (i * datetime.timedelta(days=7))).strftime('%Y%m%d')
# 주말 박스오피스는 월~일이므로 가장 최신의 일요일인 20190113을 기준으로 삼음  
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0&itemPerPage=10'
# weekGb = 월~일, itemPerPage = 최대 10개만 나오도록 지정

    res = requests.get(url)
    movie = res.json()
    # pprint(movie)

    for j in range(len(movie["boxOfficeResult"]["weeklyBoxOfficeList"])):
        if movie["boxOfficeResult"]["weeklyBoxOfficeList"][j]["movieCd"] not in movieCode:   # 영화코드가 같다면 자동적으로 앞에 있는 코드가 최신 버전의 데이터이므로 관객수는 비교 조건에 넣지 않음
            movieCode.append(movie["boxOfficeResult"]["weeklyBoxOfficeList"][j]["movieCd"])
            movieName.append(movie["boxOfficeResult"]["weeklyBoxOfficeList"][j]["movieNm"])
            watchAccount.append(movie["boxOfficeResult"]["weeklyBoxOfficeList"][j]["audiAcc"])
            countDay.append(movie["boxOfficeResult"]["showRange"][9:])

csv_writes('boxoffice.csv', movieCode, movieName, watchAccount, countDay)    # 1번 문제 csv 파일 작성   