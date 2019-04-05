# 소시지의 길이와 너비가 모두 다르다
# 높이나 너비 중 하나만 가지고 기준을 정한 다음, 오름차순으로 정렬

# 기준으로 선택하지 않은 것 중에서 첫 번째 값을 기준으로 선택
# check 배열을 하나 만들어 나보다 큰 것을 찾되, 나보다 크다면 새로운 기준으로 잡는다

# 다시 처음으로 돌아가 선택하지 않은 처음 값을 기준으로 잡고 나머지 값들과 비교한다

# 그리디는 우선 줄을 세운다 -> 기준을 잡지만, 그 기준이 영원하지 않음
# 이진탐색, 나무자르기 - 이진탐색

# DFS = B1, B2
# B4 = 순열 -> 이런 문제는 반드시 한 문제가 나온다
# B3 = 조합 기초 문제

# C9까지 조합/순열 문제이다
# C8은 이중재귀 = DFS

# D0 ~ D2 = 그래프
# D3부터 BFS 심화

# E1, E4 = 그래프 심화

# E3 = BFS -> 정보 테이블 만들기
# E5 = 중력 개념 적용

# (E7)나머지는 BFS 문제들

# mono999@naver.com
# 김은경 강사님


import sys
sys.stdin = open("F2_소시지 공장_input.txt")


N = int(input())

data = list(map(int, input().split()))

sausage = []

for i in range(0, len(data), 2):
    sausage.append([data[i], data[i+1]])

sausage.sort(key=lambda x : x[0])  # 정렬 방법 외우기

check = [0] * N
# print(sausage)

# temp = sausage[0][1]
# check[0] = 1

min_time = 0

# temp = 0

# while True:

    # for i in range(len(sausage)):
    #     if sausage[i][1] >= temp and check[i] == 0:
    #         temp = sausage[i][1]
    #         check[i] = 1
    #
    # # print(temp)
    # if sum(check) == N:
    #     break
    # else:
    #     min_time += 1
    #     for j in range(len(check)):
    #         if check[j] == 0:
    #             temp = sausage[j][1]
    #             check[j] = 1
    #             break

for i in range(N):
    if check[i] == 0:
        min_time += 1
        check[i] = 1
        temp = sausage[i][1]
    for j in range(i+1, N):
        if sausage[j][1] < temp:
            continue
        if check[j] == 0:
            temp = sausage[j][1]
            check[j] = 1

print(min_time)