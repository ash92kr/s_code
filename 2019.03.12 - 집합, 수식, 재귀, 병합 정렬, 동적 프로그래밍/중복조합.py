def myprint(q):
    while q != 0:
        q -= 1
        print(T[q], end=" ")
    print()

def H(n, r, q):
    if r == 0:
        myprint(q)
    elif n == 0:  # n = 0이 되면 고를 원소가 없다
        return
    else:
        T[r-1] = A[n-1]
        H(n, r-1, q)  # 점화식 처리
        H(n-1, r, q)

A = [1, 2, 3, 4]
T = [0, 0, 0]
H(4, 3, 3)



