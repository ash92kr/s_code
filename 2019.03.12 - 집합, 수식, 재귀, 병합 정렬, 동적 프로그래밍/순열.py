def Perm(n, r, q):

    if r == 0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):   # n-1부터 0까지 실시해야 한다
            A[i], A[n-1] = A[n-1], A[i]   # 위치 바꾼 다음에
            T[r-1] = A[n-1]
            Perm(n-1, r-1, q)
            A[i], A[n-1] = A[n-1], A[i]   # 다시 위치를 원래대로 바꿔야 한다

def myprint(q):
    while q != 0:
        q -= 1
        print(T[q], end=" ")
    print()

A = [1, 2, 3, 4]
T = [0] * 3
Perm(4, 3, 3)