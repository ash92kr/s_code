import sys
sys.stdin = open("in.txt")
def solve():
    hap=0
    for i in range(HN): #현재 집에서 고른 치킨집과 최소인 거리 찾기
        dist_min = 20*20
        for j in range(CN): #치킨집
            if not sel[j]: continue # 선택안한 치킨집이면 스킵
            dist_min = min(dist_min, arr[j][i]) # 최소거리
        hap += dist_min
    return hap

def DFS(no, cnt):
    # M개 골랐을때 고른 치킨과의 최소인 거리의 합 비교
    global sol
    if cnt==M:
        for i in range(CN): print(sel[i], end=' ')
        print()
        #hap = solve()
        #if hap<sol: sol=hap
        return
    if no>=CN: return
    # 현재 치킨집을 고르거나 고르지 않는 경우 시도
    sel[no]=1
    DFS(no+1, cnt+1)
    sel[no]=0
    DFS(no+1, cnt)

#main ----------------------
N, M = map(int, input().split())
temp = []
for i in range(N):
    temp.append(list(map(int, input().split())))
chk = []
house=[]
for i in range(N):
    for j in range(N):
        if temp[i][j]==2: # 치킨집
            chk.append((i, j))
        elif temp[i][j]==1: # 집
            house.append((i,j))
CN = len(chk) #치킨집개수
HN = len(house) #집의 개수
arr = [[0]*HN for _ in range(CN)] # 거리 기록
sel = [0]*HN # 고른 치킨집
for i in range(CN): # 행을 치킨집
    for j in range(HN):
        dist = abs(chk[i][0] - house[j][0]) + abs(chk[i][1]-house[j][1]) # 치킨집과 집과의 거리 계산
        arr[i][j] = dist
# for i in range(CN):
#     print(arr[i])
sol = 20*20
DFS(0, 0) #0행(첫번째 치킨)부터 시작, 개수는 0개
print(sol)