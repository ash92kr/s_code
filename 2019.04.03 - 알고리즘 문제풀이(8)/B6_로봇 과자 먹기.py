import sys
sys.stdin = open("B6_로봇 과자 먹기_input.txt")

def DFS(depth, hap):

    global count

    if hap > count:
        return

    if depth >= N:
        if count > hap:
            count = hap
        return

    for i in range(N):  # 과자(열)
        if check[i]:
            continue

        record[depth] = info[depth][i]   # 거리 기록
        check[i] = 1
        DFS(depth+1, hap + record[depth])   # hap + info[depth][i]도 같음
        check[i] = 0


# 거리는 x좌표와 y좌표끼리의 차에 절대값을 씌운 것
# 로봇을 행, 과자를 열에 놓고 거리를 2차원 배열에 만듦
# 순열을 사용해 최솟값을 구함

T = int(input())

for tc in range(T):

    N = int(input())

    cookie = list(map(int, input().split()))

    robot = list(map(int, input().split()))

    info = [[0 for _ in range(N)] for _ in range(N)]

    pan = [[0 for _ in range(101)] for _ in range(101)]


    for i in range(N):
        for j in range(N):
            info[i][j] = abs(robot[i*2]-cookie[j*2]) + abs(robot[(i*2)+1]-cookie[(j*2)+1])

    # print(info)

    count = 987654321

    record = [0] * N
    check = [0] * N

    DFS(0, 0)  # 현재 로봇에서 N개의 과자를 먹어보는 경우의 수(과자 중복 배제)

    print(count)