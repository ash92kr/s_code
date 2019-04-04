import sys
sys.stdin = open("in.txt")
def DFS(no, hap):
    # 현재 로봇에서 N개의 과자를 먹어보는 경우의 수 (단 과자 중복 배제)
    global sol
    if hap>sol: return # 가지치기
    if no>=N:
        # for i in range(N): print(rec[i], end=' ')
        # print(hap)
        if hap<sol:sol = hap
        return
    for i in range(N): # 과자(열)
        if chk[i]: continue
        chk[i] =1
        rec[no] = arr[no][i] # 거리 기록
        DFS(no+1, hap+arr[no][i])
        chk[i]=0

#main ---------------------------
T = int(input())
for ti in range(T):
    N = int(input())
    snack = list(map(int, input().split()))
    robot = list(map(int, input().split()))
    arr = [[0]*N for _ in range(N)]
    chk = [0]*N # 과자 중복여부 체크 배열
    rec = [0]*N # 로봇별 먹은 과자의 거리 기록배열
    for i in range(N):
        for j in range(N):
            arr[i][j] = abs(robot[i*2] - snack[j*2]) + abs(robot[i*2+1]- snack[j*2+1])
    for i in range(N):
        print(arr[i])
    sol = 0x7fffffff
    DFS(0, 0) # 0번 로봇부터 시작, 거리의 합계 0
    print(sol)