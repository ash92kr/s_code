# -*- encoding: utf-8 -*-

import requests
import csv
import json
import os
from bs4 import BeautifulSoup
from pprint import pprint

# 영화진흥위원회

private = '79b56f7867744727675c8db41a8ca6be'
itemPerPage = 100
# openStartDt = 2000
# curPage = 1

for i in range(2000, 2020):
    # for j in range(1, 11):
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={0}&itemPerPage={1}&openStartDt={2}'.format(private, itemPerPage, i)
    req = requests.get(url)
    movie = req.json()
    # pprint(movie)

    movie_code = []

    # for i in range(len(movie["movieListResult"]["movieList"])):
    for j in range(itemPerPage):
        if movie["movieListResult"]["movieList"][j]['movieCd'] not in movie_code:
            movie_code.append(movie["movieListResult"]["movieList"][j]['movieCd'])
            # print(movie_code)

print(movie_code)


# # 네이버 영화 정보
# url = "https://movie.naver.com/movie/bi/mi/media.nhn?code=136900"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')
# image = soup.select_one('#content > div.article > div.obj_section2.noline > div > div.ifr_module > div.ifr_trailer > div > ul > li > p.tx_video.ico_hd > a')

# # print(image)

# media = []
# media.append('https://movie.naver.com' + image.get('href'))


# # for link in image:
#     # print(link.get('href'))
#     # media.append(link.get('href'))

# print(media)






