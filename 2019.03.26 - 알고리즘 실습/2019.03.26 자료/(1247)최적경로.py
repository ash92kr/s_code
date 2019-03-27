import time
from time import strftime
import sys
sys.stdin = open("(1247)최적경로_input.txt", "r")
T = int(input())
def getD(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])  # 거리 계산

def perm(n, k, cur_dist):   # 순열(cur_dist는 초기값이 0이다)
    global ans
    if cur_dist > ans: return

    if k == n:
        cur_dist += D[A[k]][A[N+1]]   # 마지막 고객부터 집거리도 포함해야 한다
        if cur_dist < ans : ans = cur_dist   # 초기값보다 cur_dist가 더 작아야 한다
    else:
        for i in range(k+1, n+1, 1):   # k+1부터 N까지 순회
            A[k+1], A[i] = A[i], A[k+1]
            perm(n, k+1, cur_dist + D[A[k]][A[k+1]])  # 좌표를 통한 거리 구하기
            A[k+1], A[i] = A[i], A[k+1]

for tc in range(T):
    start_time = time.time()

    N = int(input())
    temp = list(map(int, input().split()))
    A = [0] + list(range(1, N+1, 1)) + [N+1]  # 회사-고객-집 : 따로 넣어도 되나 계산 편하게 하기 위함
    P = [(0,0) for _ in range(N+2)]          # 좌표
    D = [[0 for _ in range(N+2)] for _ in range(N+2)]  # 거리(회사, 고객, 집의 좌표를 넣음)
    ans = 0x7fffffff
    P[0] = (temp[0], temp[1])  # 회사 좌표를 처음에 넣음
    P[N+1] = (temp[2], temp[3]) # 집 좌표를 마지막에 넣음

    idx = 1
    for i in range(4, len(temp), 2): # 고객(원 데이터의 4번 인덱스부터 시작)
        P[idx] = (temp[i], temp[i+1])   # 튜플로 넣음
        idx += 1

    for i in range(N+1):   # 메모이제이션_거리계산(방향성이 없어 반만 구하면 된다)
        for j in range(i+1, N+2, 1):
            D[j][i] = D[i][j] = getD(P[i], P[j])

    perm(N, 0, 0)
    print("#{} {}".format(tc+1, ans))

print(time.time() - start_time, 'seconds')