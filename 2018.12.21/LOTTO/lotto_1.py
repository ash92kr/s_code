from bs4 import BeautifulSoup
import requests
import random

# 837회부터 최근 2달 간 로또 번호를 가져오고 싶다
numbers = random.sample(range(800, 838), 8)
print(numbers)

for number in range(len(numbers)):
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={numbers[number]}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    # lotto = soup.select('#article > div > div > div.win_result > div > div.num.win > p > span')
    bonus = soup.select_one('#article > div > div > div > div > div.num.bonus > p > span')
    print(f'{numbers[number]}회차의 당첨번호는')
    for i in soup.select('#article > div > div > div.win_result > div > div.num.win > p > span'):
        # print(i.text)
        num_lotto = i.text
        print(f'{num_lotto}', end=" ")
    print(f'이고 보너스 번호는 {bonus.text}입니다.')


# print(몇 회차 당첨번호)  1 + 2 + 3 + 4 + 5 + 6 + 7


numbers = random.sample(range(800, 838), 8)
for num in numbers:
    count = 0
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    lucky = soup.select(".ball_645")
    print(f"{num} 회차 당첨번호")
    for i in lucky:
        print(i.text, end=" ")
        count += 1
        if count == 6:
            print("+", end=" ")
    print()






