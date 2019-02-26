def selectionSort(arr, cnt):
    for i in range(cnt - 1):   # 최소값을 찾아 바꿈
        min = i   # 0번째 값을 min으로 본다
        for j in range(i+1, cnt):   # cnt = len(arr)
            x = arr[min][0] * arr[min][1]
            y = arr[j][0] * arr[j][1]
            if x > y:
                min = j   # min에 넣을 인덱스를 변경
            elif x == y and arr[min][0] > arr[j][0]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]   # 위치 변경


def get_submatrix(x, y):
    global submatrix, subcnt
    i = 0
    while data[x+i][y]:   # i = x(행), j = y(열) 
        j = 0   # 구구단과 마찬가지로 i(행/세로)에 속한 j(열/가로)을 구함
        while data[x+i][y+j]:
            data[x+i][y+j] = 0   # 행렬을 순회하면서 0으로 채움
            j += 1   # 열을 더함
        i += 1   # 행을 더함
    submatrix[subcnt][0] = i   # 행의 개수를 submatrix에 추가
    submatrix[subcnt][1] = j   # 열의 개수를 submatrix에 추가
    subcnt += 1


import sys
sys.stdin = open("(1258)행렬찾기_input.txt","r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    submatrix = [[0 for _ in range(2)] for _ in range(20)]

    subcnt = 0
    for i in range(N):
        for j in range(N):
            if data[i][j]:   # data[i][j]가 0이 아니면
                get_submatrix(i, j)   # 행렬을 찾기

    selectionSort(submatrix, subcnt)    # 선택 정렬

    print(f"#{tc+1} {subcnt}", end=" ")
    for i in range(subcnt):
        print(f"{submatrix[i][0]} {submatrix[i][1]}", end=" ")
    print()
