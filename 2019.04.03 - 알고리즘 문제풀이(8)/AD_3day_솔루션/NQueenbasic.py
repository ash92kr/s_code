import sys
sys.stdin = open("in.txt")
dr =[-1, -1, -1]
dc =[-1, 0, 1]
def check(r, c):# 현재좌표에 퀸을 놓을수 있는지 여부 체크
    for i in range(3):# 3방향
        for k in range(1, N): #1배, 2배 ... 증감치의 배수 계산
            nr = r+dr[i]*k
            nc = c+dc[i]*k
            if nr< 0 or nr>=N or nc<0 or nc>=N : break
            if arr[nr][nc]==1: return 0 # 놓을수 없음 실패
    return 1 # 퀸 놓을수 있음 성공

def DFS(no): # 현재 행에서 모든 열에 퀸을 놓아보는 경우
    global sol
    if no>=N:
        sol+=1
        return
    for i in range(N):
        if chk1[i]:continue # 세로방향체크
        if chk2[no + i]: continue  # 오른쪽대각선방향체크
        if chk3[(N-1)-(no-i)]: continue  # 왼족대각선방향체크
        chk1[i]=chk2[no + i]=chk3[(N-1)-(no-i)]=1
        DFS(no+1)
        chk1[i] = chk2[no + i] = chk3[(N - 1) - (no - i)] = 0

        # for i in range(N): # 열
    #     if check(no, i): # 퀸을 놓을수 있으면
    #         arr[no][i]=1 # 퀸놓기
    #         DFS(no+1)
    #         arr[no][i]=0 # 퀸 빼기



#main -------------------------
N = int(input())
arr = [[0]*N for _ in range(N)]
chk1 = [0]*N
chk2 = [0]*N*2
chk3 = [0]*N*2
sol=0
DFS(0)# 0행부터 시작
print(sol)