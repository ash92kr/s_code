import sys
sys.stdin = open("in.txt")
def DFS(start, cnt):
    global sol
    if cnt==M:
        for i in range(cnt): print(rec[i], end=' ')
        print()
        sol+=1
        return
    for i in range(start, N): #흙의 재료
        if rec[cnt] == arr[i]: continue # 같은재료이면 스킵
        rec[cnt]=arr[i]
        DFS(i+1, cnt+1)
    rec[cnt] = 0 # 현재 모든 시도가 끝나면 현재 재료 지우기

T = int(input())
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
rec = [0]*N
sol=0
DFS(0, 0) # 0번요소부터시작, 개수는 0개
print(sol)
