import sys
sys.stdin = open("in.txt")
def DFS(no, Lsum, Rsum):
    global sol
    if sol: return #가지치기
    if no>=CN:
        if Lsum==Rsum: sol=1    # 양쪽저울무게가 같은면 성공
        return
    # 현재 추를 사용하거나(왼쪽, 오른쪽저울에 사용) 사용하지 않기
    DFS(no+1, Lsum+chu[no], Rsum) # 현재추를 왼쪽에 올리기
    DFS(no+1, Lsum, Rsum+chu[no])  # 현재추를 오른쪽에 올리기
    DFS(no+1, Lsum, Rsum)  # 현재추를 사용하지 않기

#main --------------------------
CN = int(input())
chu = list(map(int, input().split()))
BN = int(input())
ball = list(map(int, input().split()))
rec = [0]*CN #기록배열
for i in range(BN):
    sol=0
    DFS(0, ball[i], 0) # 0번추부터시작, 왼쪽저울무게를 구슬로 초기화, 오른저울무게 0
    if sol:print('Y')
    else: print('N')

