import sys
sys.stdin = open("달팽이사각형_input.txt")

N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

r = 0
c = -1
num = 0   # 카운팅할 숫자
cnt = N   # 방향별 반복 횟수

while num < N*N:

    # 오른쪽 이동
    for i in range(cnt):
        c += 1   # 열 좌표만 증가(오른쪽 이동)
        num += 1
        arr[r][c] = num
    cnt -= 1

    # 아래쪽 이동
    for i in range(cnt):
        r += 1
        num += 1
        arr[r][c] = num

    # 왼쪽 이동
    for i in range(cnt):
        c -= 1
        num += 1
        arr[r][c] = num

    cnt -= 1

    # 위쪽 이동
    for i in range(cnt):
        r -= 1
        num += 1
        arr[r][c] = num


for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()
