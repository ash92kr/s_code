import requests  # 주소를 받아온다

req = requests.get("https://finance.naver.com/sise/").text   # 응답
# print(requests.get("https://www.naver.com"))
# print(requests.get("https://www.naver.com").text)  # html 소스 - 페이지 소스 보기
# print(requests.get("https://www.naver.com").status_code)   # 상태 코드 숫자만 보여준다

from bs4 import BeautifulSoup   # as bus
# BeautifulSoup 상단에 더 큰 패키지가 있다면 bs4를 쓴다
# import bs4.BeautifulSoup 로 적어야 한다 -> 단, 함수를 불러올 때 모두 적어야 한다

soup = BeautifulSoup(req, 'html.parser')   # 꾸며줌
# id는 중복될 수 없고 class는 중복될 수 있으므로 id를 기반으로 스크래핑해야 한다
# copy - copy selector

kospi = soup.select_one("#KOSPI_now")   # 코스피 지수가 있는 경로 - 하나만 선택
print(kospi)
print(kospi.text)





