def get_submatrix(x, y):
    global submatrix, subcnt
    i = 0
    while data[x+i][y]:
        j = 0
        while data[x+i][y+j]:
            data[x+i][y+j] = 0
            j += 1
        i += 1
    submatrix.append((i, j))   # 튜플 저장


import sys
sys.stdin = open("(1258)행렬찾기_input.txt","r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    submatrix = []

    # subcnt = 0
    for i in range(N):
        for j in range(N):
            if data[i][j]:
                get_submatrix(i, j)

    submatrix.sort(key=lambda a:(a[0]*a[1], a[0]))   # 람다 함수
    # a 함수는 a[0]*a[1]을 곱한 값 기준, a[0]이 작은 것을 먼저 배치할 것

    print(f"#{tc+1} {len(submatrix)}", end=" ")
    for x, y in submatrix:
        print(f"{x} {y}", end=" ")
    print()
