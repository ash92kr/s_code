import requests
import csv
import datetime
import json
from pprint import pprint
import os


def csv_reads(file_name, *row):
    
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            print(row[start_row])


movie_code = csv_reads('boxoffice.csv')[1:]  # 43개의 영화코드 저장
movie_name_ko = []
movie_name_en = []
movie_name_og = []
prdt_year = []
show_Tm = []
genres = []
directors = []
watch_grade_nm = []
actors = []
actor1 = []
actor2 = []
actor3 = []


for i in range(len(movie_code)):

    key = os.getenv("key_bot")
    code = movie_code[i]          # code = '20183915'   # 애니메이션 코드
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={code}'

    res = requests.get(url)
    movieInfo = res.json()
    # pprint(movieInfo)

    movie_name_ko.append(movieInfo['movieInfoResult']['movieInfo']['movieNm'])   # 영화명(국문)
    movie_name_en.append(movieInfo['movieInfoResult']['movieInfo']['movieNmEn'])   # 영화명(영문)
    movie_name_og.append(movieInfo['movieInfoResult']['movieInfo']['movieNmOg'])   # 영화명(원문)
    prdt_year.append(movieInfo['movieInfoResult']['movieInfo']['prdtYear'][:4])   # 개봉연도   
    show_Tm.append(movieInfo['movieInfoResult']['movieInfo']['showTm'])   # 상영시간
    genres.append(movieInfo['movieInfoResult']['movieInfo']['genres'][0]['genreNm'])   # 장르
    directors.append(movieInfo['movieInfoResult']['movieInfo']['directors'][0]['peopleNm'])   # 감독명
    watch_grade_nm.append(movieInfo['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm'])   # 관람등급

    if len(movieInfo['movieInfoResult']['movieInfo']['actors']) >= 3:
        for j in range(0, 3):
            actors.append(movieInfo['movieInfoResult']['movieInfo']['actors'][j]['peopleNm'])
    elif len(movieInfo['movieInfoResult']['movieInfo']['actors']) == 2:
        for j in range(0, 2):
            actors.append(movieInfo['movieInfoResult']['movieInfo']['actors'][j]['peopleNm'])
        actors.append('')
    elif len(movieInfo['movieInfoResult']['movieInfo']['actors']) == 1:
        for j in range(0, 1):
            actors.append(movieInfo['movieInfoResult']['movieInfo']['actors'][j]['peopleNm'])
        actors.append('')
        actors.append('')
    else:
        actors.append('')
        actors.append('')
        actors.append('')


for i in range(len(actors)):
    if i % 3 == 0:
        actor1.append(actors[i])
    elif i % 3 == 1:
        actor2.append(actors[i])
    elif i % 3 == 2:
        actor3.append(actors[i])


def csv_writes(file_name, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12):

    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ('movie_code', 'movie_name_ko', 'movie_name_en', 'movie_name_og', 'prdt_year', 'show_Tm', 'genres', 'directors', 'watch_grade_nm', 'actor1', 'actor2', 'actor3')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(len(list1)):
            writer.writerow({'movie_code': list1[i], 'movie_name_ko': list2[i], 'movie_name_en': list3[i],
            'movie_name_og': list4[i], 'prdt_year': list5[i], 'show_Tm': list6[i], 'genres': list7[i], 'directors': list8[i],
            'watch_grade_nm': list9[i], 'actor1': list10[i], 'actor2': list11[i], 'actor3': list12[i] })


csv_writes('movie.csv', movie_code, movie_name_ko, movie_name_en, movie_name_og, prdt_year, show_Tm,
           genres, directors, watch_grade_nm, actor1, actor2, actor3) 
