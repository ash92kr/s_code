import random
import requests
import json
from pprint import pprint

# 1. random으로 로또번호 생성하기

# original = list(range(1, 46))
# my_pur = sorted(random.sample(original, 6))

# my_pur2 = set(my_pur)
# print(my_pur2)

# 2. api를 통해 우승 번호를 가져온다

# 2-1 url 요청 보내서 정보를 json으로 가져온다(딕셔너리 접근)

# url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
# res = requests.get(url)
# print(res)
# print(type(res))   # string type

# lotto = res.json()
# pprint(lotto)
# print(type(lotto))   # dictionrary type

# 2-2 api의 당첨번호와 보너스 번호를 저장한다

# no1 = lotto["drwtNo1"]
# no2 = lotto["drwtNo2"]
# no3 = lotto["drwtNo3"]
# no4 = lotto["drwtNo4"]
# no5 = lotto["drwtNo5"]
# no6 = lotto["drwtNo6"]

# bonus = lotto["bnusNo"]

# api = set([no1, no2, no3, no4, no5, no6])
# bonus2 = set([bonus])
# print(api)
# print(bonus2)

# 3. 1번과 2번을 비교해 내 등수를 알려준다

# inter = my_pur2 & api

# if len(inter) == 3:
#     print("축하합니다! 5등에 당첨되었습니다. 상금은 5000원입니다.")
# elif len(inter) == 4:
#     print("축하합니다! 4등에 당첨되었습니다. 상금은 50000원입니다.")
# elif len(inter) == 5:
#     if len(my_pur2 & bonus) == 0:
#         print("축하합니다! 3등에 당첨되었습니다. 상금은 가까운 은행에서 수령하세요.")
#     else:
#         print("축하합니다! 2등에 당첨되었습니다. 상금은 가까운 은행에서 수령하세요.")
# elif len(inter) == 6:
#     print("축하합니다! 1등에 당첨되었습니다. 상금은 가까운 은행에서 수령하세요.")
# else:
#     print("안타깝습니다. 다음에 다시 도전해주세요.")


# 4. 위 과정을 반복하시오

# url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
# res = requests.get(url)
# lotto = res.json()

# no1 = lotto["drwtNo1"]
# no2 = lotto["drwtNo2"]
# no3 = lotto["drwtNo3"]
# no4 = lotto["drwtNo4"]
# no5 = lotto["drwtNo5"]
# no6 = lotto["drwtNo6"]

# no7 = lotto["bnusNo"]

# api = set([no1, no2, no3, no4, no5, no6])
# bonus = set([no7])

# count = 0

# while True:
#     original = list(range(1, 46))
#     my_pur = set(random.sample(original, 6))
    
#     inter = my_pur & api

#     if len(inter) == 3:
#         print("축하합니다! 5등에 당첨되었습니다. 상금은 5000원입니다.")
#     elif len(inter) == 4:
#         print("축하합니다! 4등에 당첨되었습니다. 상금은 50000원입니다.")
#     elif len(inter) == 5:
#         if len(my_pur & bonus) == 0:
#             print("축하합니다! 3등에 당첨되었습니다. 상금은 가까운 은행에서 수령하세요.")
#         else:
#             print("축하합니다! 2등에 당첨되었습니다. 상금은 가까운 은행에서 수령하세요.")
#     elif len(inter) == 6:
#         print("축하합니다! 1등에 당첨되었습니다. 상금은 가까운 은행에서 수령하세요.")
#         print(my_pur, count)
#         break
#     else:
#         print("안타깝습니다. 다음에 다시 도전해주세요.")
#     count += 1
#     print(count)





url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

winner = []
for i in range(1, 7):
    winner.append(lotto[f"drwtNo{i}"])

bonus = lotto["bnusNo"]
print("보너스 번호: " + str(bonus))
print("이번 주 당첨번호: " + str(winner))

count = 0
while True:  # False가 되었을 때 while문이 멈춘다
    count += 1
    my_numbers = sorted(random.sample(range(1, 46), 6))   # tap을 누르면 우측, shift+tab을 누르면 좌측으로 이동
    matched = len(set(winner) & set(my_numbers))   # alt+화살표 키 : 줄 이동, alt+shift+방향키 : 줄 단위 복사
                                                # 변수명 + ctrl+d : 한 번에 여러 단어 바꾸기
    if matched == 6:                            # alt + ctrl : 멀티 커서(여러 줄을 한번에 바꿈)
        print("1등")
    elif matched == 5:
        if bonus in my_numbers:
            print("2등")
        else:
            print("3등")
    elif matched == 4:
        print("4등")
    elif matched == 3:
        print("5등")
        print(count, "번만에 당첨되었습니다")
        # print(count * 1000, "원 써서 먹었습니다")
        money = format(count*1000, ',')
        print("쓴 돈은", money)
        break
    else:
        print("응 안돼 돌아가")
