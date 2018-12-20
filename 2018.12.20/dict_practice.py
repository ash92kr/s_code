"""
파이썬 dictionary 활용 기초
"""

dict = {
    "대전": 23,
    "서울": 30,
    "구미": 20
}

print(dict.values())
# dictionary의 값을 가져온다 -> 리스트가 아니라 for문을 사용해야 한다
print(type(dict.values()))   # class 객체

list = [1, 2313, "123945"]
print(len(list))   # 요소의 개수를 알려주는 len 함수

# 1. 평균 구하기
score = {
    "국어" : 87,
    "영어" : 92,
    "수학" : 40
}

print(score.values())
print(score.keys())


# for문을 사용해서 평균 구하기
sc = 0    # 변수에 초기값 할당

for i in score.values():
    sc = sc + i   # sc += i

average = sc / len(score.values())
print(average)


# for문을 사용하지 않고 풀기
print(sum(score.values()) / len(score.values()))



# 2. 반 평균을 구하시오
scores = {
    "철수": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "영희": {
        "수학": 70,
        "국어": 60,
        "음악": 50
    }
}

sum_su = 0
sum_hee = 0

# 첫 번째 방법 - for문을 1번만 사용
print(scores["철수"].values())

for i in scores["철수"].values():
    sum_su = sum_su + i

for i in scores["영희"].values():
    sum_hee = sum_hee + i

average_su = sum_su / len(scores["철수"].values())
average_hee = sum_hee / len(scores["영희"].values())
print(average_su)
print(average_hee)

# 두 번째 방법 - for문을 2번 사용

print(scores.values())
print(scores.keys())

ban = 0
count = 0

for i in scores.keys():
    for j in scores[i].values():
        ban = ban + j
        count = count + 1

print(count)

average = ban / count
print(average)



# all_total = 0
# for score in scores.values():
#     totals = score.values()
#     for total in totals:
#         all_total = all_total + total
# print(all_total)


# total_score = 0
# count = 0
# for person_score in scores.values():
#     for individual_score in person_score.values():
#         total_score = total_score + individual_score
#         count = count + 1

# average_score = total_score / count



# 3
scores = {
    "국어": 87,
    "영어": 92,
    "수학": 40
}

# 여기서의 핵심은 items를 써야 한다는 것!
for key, value in scores.items():
    print(key)
    print(value)

# 3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}


max_temp = []
min_temp = []   

for name, temp in cities.items(): 
    max_temp.append(max(temp))
    min_temp.append(min(temp))
    if max_temp == max(max_temp):
        print(name)
    elif min_temp == min(min_temp):
        print(name)



hot = 0
cold = 0
hot_city = ""  # 빈 스트링
cold_city = ""
count == 0

for name, temp in cities.items():
    if count == 0:   # 무조건 한 번은 실행되도록 함
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:   # 비교 대상이 있으므로 아래를 실행
        if min(temp) < cold:   # 현재 온도보다 추우면 최소온도로 넣음
            cold = min(temp)
            cold_city = name
        if max(temp) > hot:   # 현재 온도보다 높으면 최대온도로 넣음
            hot = max(temp)
            hot_city = name
    count += 1

print(hot_city)
print(cold_city)

