import requests
import csv
# from bs4 import BeautifulSoup
import datetime
import json
from pprint import pprint

# for i in range(10):
#     latest = datetime.date(2019, 1, 13)
#     targetDt = latest - (i * datetime.timedelta(days=7))
#     print(targetDt)

# for i in range(1):
#     key = '79b56f7867744727675c8db41a8ca6be'

#     latest = datetime.date(2019, 1, 13)
#     targetDt = (latest - (i * datetime.timedelta(days=7))).strftime('%Y%m%d')

#     url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'

#     res = requests.get(url)
#     movie = res.json()

#     pprint(movie)


def csv_reads(file_name, *row):
    
    movie_attract = []

    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            movie_attract.append(line.strip().split(',')[0]) # 개행 문자를 없애기 위해 strip() 필요

    return movie_attract

movie_code = csv_reads('boxoffice.csv')[1:]
print(movie_code)

