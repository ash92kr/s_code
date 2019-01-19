import requests
import csv
# from bs4 import BeautifulSoup
import datetime
import json
from pprint import pprint
import os

# def csv_writes(file_name, list1, list2, list3, list4):
    
#     with open(file_name, 'w', newline='', encoding='utf-8') as f:
#         fieldnames = ('movie_code', 'title', 'audience', 'recorded_at')
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()

#         for i in range(len(list1)):
#             writer.writerow({'movie_code': list1[i], 'title': list2[i], 'audience': list3[i], 'recorded_at': list4[i]})

# # def csv_writes(file_name, my_dict):

# #     with open(file_name, 'w', encoding='utf-8') as f:
# #         for item in my_dict.items():
# #             f.write(f'{item[0]}')
# #             f.write(f'{item[1]}\r\n')


# def csv_reads(file_name, *row):
    
#     movie_attract = []

#     with open(file_name, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#         for line in lines:
#             movie_attract.append(line.strip().split(',')[0]) # 개행 문자를 없애기 위해 strip() 필요

#     return movie_attract



# def csv_reads(file_name, *row):
    
#     with open(file_name, newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
        
#         for row in reader:
#             print(row[start_row])


# # question1
# movieCode = []   # 영화 대표코드
# movieName = []   # 영화명
# watchAccount = []   # 해당일 누적관객수
# countDay = []   # 해당일

# for i in range(10):
#     key = os.getenv("key_bot")
# # 본인의 개인키
#     latest = datetime.date(2019, 1, 13)
#     targetDt = (latest - (i * datetime.timedelta(days=7))).strftime('%Y%m%d')
# # 주말 박스오피스는 월~일이므로 가장 최신의 일요일인 20190113을 기준으로 삼음  
#     url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0&itemPerPage=10'
# # weekGb = 월~일, itemPerPage = 최대 10개만 나오도록 지정

#     res = requests.get(url)
#     movie = res.json()
#     # pprint(movie)

#     # movie2 = movie["boxOfficeResult"]["weeklyBoxOfficeList"]   # 앞 딕셔너리 제거
#     # pprint(movie2)

#     for j in range(len(movie["boxOfficeResult"]["weeklyBoxOfficeList"])):
#         if movie["boxOfficeResult"]["weeklyBoxOfficeList"][j]["movieCd"] not in movieCode:   # 영화코드가 같다면 자동적으로 앞에 있는 코드가 최신 버전의 데이터이므로 관객수는 비교 조건에 넣지 않음
#             movieCode.append(movie["boxOfficeResult"]["weeklyBoxOfficeList"][j]["movieCd"])
#             movieName.append(movie["boxOfficeResult"]["weeklyBoxOfficeList"][j]["movieNm"])
#             watchAccount.append(movie["boxOfficeResult"]["weeklyBoxOfficeList"][j]["audiAcc"])
#             countDay.append(movie["boxOfficeResult"]["showRange"][9:])

# # movieCode = sorted(movieCode)

# csv_writes('boxoffice.csv', movieCode, movieName, watchAccount, countDay)    # 1번 문제 csv 파일 작성   



# ## question2
# movie_code = csv_reads('boxoffice.csv')[1:]  # 43개의 영화코드 저장
# movie_name_ko = []
# movie_name_en = []
# movie_name_og = []
# prdt_year = []
# show_Tm = []
# genres = []
# directors = []
# watch_grade_nm = []
# actors = []
# actor1 = []
# actor2 = []
# actor3 = []

# for i in range(len(movie_code)):
# # # for i in range(1):

#     key = os.getenv("key_bot")
#     code = movie_code[i]          # code = '20183915'   # 애니메이션 코드
#     url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={code}'

#     res = requests.get(url)
#     movieInfo = res.json()
#     # pprint(movieInfo)

#     movie_name_ko.append(movieInfo['movieInfoResult']['movieInfo']['movieNm'])   # 영화명(국문)
#     movie_name_en.append(movieInfo['movieInfoResult']['movieInfo']['movieNmEn'])   # 영화명(영문)
#     movie_name_og.append(movieInfo['movieInfoResult']['movieInfo']['movieNmOg'])   # 영화명(원문)
#     prdt_year.append(movieInfo['movieInfoResult']['movieInfo']['prdtYear'][:4])   # 개봉연도   
#     show_Tm.append(movieInfo['movieInfoResult']['movieInfo']['showTm'])   # 상영시간
#     genres.append(movieInfo['movieInfoResult']['movieInfo']['genres'][0]['genreNm'])   # 장르
#     directors.append(movieInfo['movieInfoResult']['movieInfo']['directors'][0]['peopleNm'])   # 감독명
#     watch_grade_nm.append(movieInfo['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm'])   # 관람등급

#     if len(movieInfo['movieInfoResult']['movieInfo']['actors']) >= 3:
#         for j in range(0, 3):
#             actors.append(movieInfo['movieInfoResult']['movieInfo']['actors'][j]['peopleNm'])
#     elif len(movieInfo['movieInfoResult']['movieInfo']['actors']) == 2:
#         for j in range(0, 2):
#             actors.append(movieInfo['movieInfoResult']['movieInfo']['actors'][j]['peopleNm'])
#         actors.append('')
#     elif len(movieInfo['movieInfoResult']['movieInfo']['actors']) == 1:
#         for j in range(0, 1):
#             actors.append(movieInfo['movieInfoResult']['movieInfo']['actors'][j]['peopleNm'])
#         actors.append('')
#         actors.append('')
#     else:
#         actors.append('')
#         actors.append('')
#         actors.append('')


# for i in range(len(actors)):
#     if i % 3 == 0:
#         actor1.append(actors[i])
#     elif i % 3 == 1:
#         actor2.append(actors[i])
#     elif i % 3 == 2:
#         actor3.append(actors[i])


# #     # count = 0
# #     # while count < 3:
# #     #     if len(movieInfo['movieInfoResult']['movieInfo']['actors'][0]) >= 3:
# #     #         for j in range(len(movieInfo['movieInfoResult']['movieInfo']['actors'][0])):
# #     #             actors.append(movieInfo['movieInfoResult']['movieInfo']['actors'][j]['peopleNm'])   # 배우(최대 3명)
# #     #             count += 1
# #     #     else:
# #     #         try:
# #     #             for j in range(len(movieInfo['movieInfoResult']['movieInfo']['actors'][0])):
# #     #                 actors.append(movieInfo['movieInfoResult']['movieInfo']['actors'][j]['peopleNm'])
# #     #                 count += 1
# #     #         except IndexError:
# #     #             actors.append('')
# #     #             count += 1


# # # print(movie_code)
# # # print(movie_name_ko)
# # # print(movie_name_en)
# # # print(movie_name_og)
# # # print(prdt_year)
# # # print(show_Tm)
# # # print(geners)
# # # print(directors)
# # # print(watch_grade_nm)
# # print(actors)
# # print(actor1)
# # print(actor2)
# # print(actor3)
# # # print(len(actors))

# # movie_api = {'movie_code': movie_code,
# #         'movie_name_ko': movie_name_ko,
# #         'movie_name_en': movie_name_en,
# #         'movie_name_og': movie_name_og,
# #         'prdt_year': prdt_year,
# #         'show_Tm': show_Tm,
# #         'geners': geners,
# #         'directors': directors,
# #         'watch_grade_nm': watch_grade_nm,
# #         'actor1': actor1,
# #         'actor2': actor2,
# #         'actor3': actor3}


# def csv_writes(file_name, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12):

#     with open(file_name, 'w', newline='', encoding='utf-8') as f:
#         fieldnames = ('movie_code', 'movie_name_ko', 'movie_name_en', 'movie_name_og', 'prdt_year', 'show_Tm', 'genres', 'directors', 'watch_grade_nm', 'actor1', 'actor2', 'actor3')
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()

#         for i in range(len(list1)):
#             writer.writerow({'movie_code': list1[i], 'movie_name_ko': list2[i], 'movie_name_en': list3[i],
#             'movie_name_og': list4[i], 'prdt_year': list5[i], 'show_Tm': list6[i], 'genres': list7[i], 'directors': list8[i],
#             'watch_grade_nm': list9[i], 'actor1': list10[i], 'actor2': list11[i], 'actor3': list12[i] })


# csv_writes('movie.csv', movie_code, movie_name_ko, movie_name_en, movie_name_og, prdt_year, show_Tm,
#            genres, directors, watch_grade_nm, actor1, actor2, actor3) 



# question3

from urllib import parse, request

movie_code = csv_reads('boxoffice.csv')[1:]

def search_movie_by_title(title) :
    client_id = os.getenv("naver_id_bot")
    client_pw = os.getenv("naver_pw_bot")
    
    enc_text = parse.quote(title)   # 변수 title을 URL 인코딩

url = f"https://openapi.naver.com/v1/search/movie.json?query={movie_name}&display=10&start=1"

req = request.Request(url)    # urllib.request.Request로 http 요청 객체 생성
req.add_header("X-Naver-Client-Id", client_id)
req.add_header("X-Naver-Client-Secret", client_pw)   # header로 id와 secret 추가


try:
        response = request.urlopen(req) 
		# 객체를 매개변수로 request.urlopen을 호출해 Web 서버에 요청
    except:
        print("책 제목 {} 검색 불가".format(title))
        return None

    res_code = response.getcode() # response의 코드

    if (res_code == 200): # 200 OK 이면
        response_body = response.read()

        print("body " + response_body.decode('utf-8') # 내용을 출력
    





