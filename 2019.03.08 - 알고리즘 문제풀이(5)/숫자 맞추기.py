import sys
sys.stdin = open("숫자 맞추기_input.txt")

def check(temp):

    global score

    for i in range(len(temp)):   # temp를 순회하면서 count가 2개 이상인 경우는 0점을 줌
        if temp.count(temp[i]) >= 2:
            score[i] += 0
        else:
            score[i] += temp[i]


N = int(input())

card = []

for i in range(N):
    card.append(list(map(int, input().split())))

score = [0] * N

for i in range(3):   # 열의 경우(3번 게임 반복)
    temp = []
    for j in range(N):   # 행의 경우(N명이 게임 실시)
        temp.append(card[j][i])   # 같은 게임의 결과를 temp에 넣음
    check(temp)


for i in range(len(score)):   # 출력
    print(score[i])