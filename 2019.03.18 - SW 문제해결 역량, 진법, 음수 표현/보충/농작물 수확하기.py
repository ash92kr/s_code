import sys
sys.stdin = open("농작물 수확하기_input.txt")

T = int(input())

for tc in range(T):

    N = int(input())

    farm = []

    for i in range(N):
        farm.append(list(map(int, input())))

    money = 0
    idx = -1
    mid = N//2
    start = mid   # 이렇게 변수를 주면서 증감시키는 것이 더 효율적이다

    for i in range(N):
        if i <= N//2:
            idx += 2  # 몇 번 반복하는가?
            for j in range(idx):
                money += farm[i][start+j]
            start -= 1   # 시작점 변경
            if i == N//2:
                start = 1   # 초기화
        else:
            idx -= 2   # 몇 번 반복하는가?
            for j in range(idx):
                money += farm[i][start+j]
            start += 1

    print("#{} {}".format(tc+1, money))




