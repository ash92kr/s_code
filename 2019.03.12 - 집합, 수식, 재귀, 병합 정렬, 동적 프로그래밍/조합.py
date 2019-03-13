def myprint(q):
    while q != 0:
        q -= 1
        print(T[q], end=" ")
    print()

def combination(n, r, q):
    if r == 0:
        myprint(q)   # 프린트 함수 부르기
    else:
        if n < r:   # n보다 r이 크면 무시
            return
        else:
            T[r-1] = A[n-1]  # A의 원소를 T에 넣음
            combination(n-1, r-1, q)  # 좌우로 갈림
            combination(n-1, r, q)

# 4개 중 3개 원소 고르기 -> 50개가 되면 재귀로 못 구하므로 memoization 처리(2차원 배열)해야 함
A = [1, 2, 3, 4]
T = [0, 0, 0]
combination(4, 3, 3)



