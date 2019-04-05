import sys
sys.stdin = open("in.txt")
def check1(sr, sc):
    step=0
    cnt=0
    for i in range(sr-R, sr+R+1):
        for j in range(sc-step, sc+step+1):
            if i<0 or i>=N or j<0 or j>=N: continue
            if arr[i][j]: continue
            arr[i][j]=2
            cnt+=1
        if i>=sr: step-=1
        else: step+=1
    return cnt

def check2(sr, sc):
    step=0
    cnt=0
    for i in range(sr-R, sr+R+1):
        for j in range(sc-step, sc+step+1):
            if i < 0 or i >= N or j < 0 or j >= N: continue
            if arr[i][j]: continue
            cnt+=1
        if i>=sr: step-=1
        else: step+=1
    return cnt


def update():
    for i in range(N*N):
            arr[i//N][i%N] = Barr[i//N][i%N]


#-----------------------------------------
N = int(input())
R = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
Barr=[[0]*N for _ in range(N)]

for i in range(N * N):
    Barr[i // N][i % N] = arr[i // N][i % N]


sol=0
for i in range(N*N):
    cnt1 = check1(i//N, i%N )
    for j in range(i+1, N*N):
        if i//N == j//N and i%N>=j%N : continue
        cnt2=check2(j//N, j%N)
        if cnt1+cnt2>sol: sol=cnt1+cnt2
    update()

print(sol)

