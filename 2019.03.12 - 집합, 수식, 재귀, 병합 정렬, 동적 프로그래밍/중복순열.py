def Perm(n, r, q):

    if r == 0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):
            A[i], A[n-1] = A[n-1], A[i]
            T[r-1] = A[n-1]
            Perm(n, r-1, q)   # 이것만 바꾸면 된다
            A[i], A[n-1] = A[n-1], A[i]


def myprint(q):
    while q != 0:
        q -= 1
        print(T[q], end=" ")
    print()


A = [1, 2, 3, 4]
T = [0] * 3   # 중복순열은 T가 A의 개수보다 커질 수 있다(4개 중에서 5개 뽑기)
Perm(4, 3, 3)