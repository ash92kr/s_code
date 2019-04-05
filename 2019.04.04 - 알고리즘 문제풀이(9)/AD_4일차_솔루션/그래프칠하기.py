import sys
sys.stdin = open("in.txt")
def check(no, color):
    #현재노드와 연결된 노드와 중복색상 여부 체크
    for i in range(no): #연결된 노드(열)
        if arr[no][i] and rec[i]==color: return 0 #연결된 노드와 같은 색이면 실패
    return 1

def DFS(no):
    global flag
    if no>=N:
        flag=1
        return
    #현재 노드에게 1~M색상을 칠해보는 경우의 수
    for i in range (1, M+1):
        if check(no, i): #현노드에게 칠할수 있으면 기록하고 다음 노드로
            rec[no] = i #색상 기록
            DFS(no+1)
            if flag: return
#main----------------------------------
N, M = map(int, input().split())
rec=[0]*N # 색상기록
arr =[] # 인접행렬
for i in range(N): # 0행0열부터 사용
    arr.append(list(map(int, input().split())))

flag=0
DFS(0) # 첫번째 노드부터 시작
if flag: #성공
    for i in range(N):
        print(rec[i], end=' ')
else: print(-1) #실패

