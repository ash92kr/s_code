a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3

def DFS(no, start):
# 1] 리턴조건 : N번째이면 리넡
    for i in range(N): print(b[i], end=' ')
    print()
    if no>=N or start>=N:
        return
    for i in range(start, N): # a[i]
        b[no]=a[i]
        DFS(no+1, i+1)
        b[no]=0

# main ============================
DFS(0, 0) # b[0] 담기 시작, a[0]구슬부터 시작