import sys
sys.stdin = open("in.txt")
dr =(0, 1, 0, -1) # 오른 아래 왼 위 순서로
dc = (1, 0, -1, 0)
def DFS(r, c):
    global sol
    if rec[r][c]>sol : return # 가지치기
    if r==N-1 and c==N-1: #도착하면 최소비용 비교
        if rec[N-1][N-1]<sol: sol = rec[N-1][N-1]
        return
    for i in range(4): # 4방향 탐색
        nr = r+dr[i]
        nc= c+dc[i]
        if nr<0 or nr>=N or nc<0 or nc>=N : continue
        #  가볼위치의 이전의 해 > 현재진행경로의 해 비교하여 최소이면 기록하고 다음위치로 이동
        if rec[nr][nc] > rec[r][c]+arr[nr][nc]: # 현재 경로해가 더 최소이면
            rec[nr][nc] = rec[r][c] + arr[nr][nc]
            DFS(nr, nc)
def BFS():
    que=[]
    #1] 시작점 큐에저장(기록)
    que.append((0, 0))
    rec[0][0]=arr[0][0]
    while que:
        #2] 큐에서 데이타 읽기
        r, c = que.pop(0)
        #3] 연결점 찾아 큐에저장(기록)
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if nr<0 or nr>=N or nc<0 or nc>=N : continue #범위를 벗어나면 스킵
            #가볼위치의 이전의 해 > 현재진행경로의 해 비교하여 최소이면
            if rec[nr][nc] > rec[r][c] + arr[nr][nc]:
                rec[nr][nc] = rec[r][c] + arr[nr][nc]
                que.append((nr, nc))
    #4] 큐가 빈상태
    return rec[N-1][N-1]
#main -----------------
N = int(input())
arr = []
rec = [[100000]*N for _ in range(N)] # 자외선합 기록
for i in range(N):
    arr.append(list(map(int, input())))
#sol=10*100*100
#rec[0][0]=0 #시작점 값 기록
#DFS(0, 0)
sol = BFS()
print(sol)


