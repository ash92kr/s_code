import sys
sys.stdin = open("미로탈출 로봇_input.txt")

N = int(input())
arr = [[1]*(N+2) for _ in range(N+2)]  # 가장자리 1로 채움
for i in range(1, N+1):  # 1행 1열부터 데이터 입력받기
    arr[i] = [1] + list(map(int, input())) + [1]

Darr = list(map(int, input().split()))  # 방향 순서 배열

# for i in range(len(arr)):
#     print(arr[i])

Dno = 0   # Darr의 인덱스 번호(방향 순서)
dr = [0, 1, 0, -1, 0]  # 아래쪽, 왼쪽, 위쪽, 오른쪽 방향
dc = [0, 0, -1, 0, 1]

r, c = 1, 1
cnt = 0

while True:
    # 좌표계산
    r += dr[Darr[Dno]]   # Darr의 인덱스 순서대로 받기
    c += dc[Darr[Dno]]

    if arr[r][c] == 0:   # 0이면 방문표시하고 카운트
        arr[r][c] = 9
        cnt += 1
    elif arr[r][c] == 1:  # 1이면 이전좌표로 이동하고 방향전환(방향 로테이션)
        r -= dr[Darr[Dno]]
        c -= dc[Darr[Dno]]   # Darr의 인덱스만큼 빼기
        Dno += 1   # 인덱스가 4가 되면 0으로 되돌림
        if Dno == 4:
            Dno = 0
        # Dno = (Dno+1) % 4
    else:   # 지나간 자리면 탈출
        break
    # print(r, c)

print(cnt)

