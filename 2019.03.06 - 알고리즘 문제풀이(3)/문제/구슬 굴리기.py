import sys
sys.stdin = open("구슬 굴리기_input.txt")

r, c = map(int, input().split())   # 전체 행/열 개수

marvel = [[1] * (r+2) for i in range(c+2)]   # 구슬이 굴러가는 판을 모두 1로 채움 - 1

for i in range(1, r+1):
    marvel[i] = [1] + list(map(int, input())) + [1]  # 행의 시작과 끝에 1을 채우고, 0/N+2는 비워 놓음 - 2

N = int(input())
direct = list(map(int, input().split()))   # 방향 배열

# for i in range(len(marvel)):
#     print(marvel[i])

x = 0
y = 0
count = 0  # 방향 배열 변수

for i in range(1, r+1):
    for j in range(1, c+1):
        if marvel[i][j] == 2:
            x, y = i, j   # x, y 구하기

length = 1   # 전체 길이는 1로 시작(시작점을 9로 바꾸기 때문)
marvel[x][y] = 9

dx = [0, -1, 1, 0, 0]   # 시작점을 0으로 놓아야 한다!
dy = [0, 0, 0, -1, 1]   # 위쪽, 아래쪽, 왼쪽, 오른쪽

while True:

    x += dx[direct[count]]   # 행 좌표 변경
    y += dy[direct[count]]   # 열 좌표 변경

    # print(x, y)

    if marvel[x][y] == 0:   # 0이면 9로 바꾸고 이동 거리에 1 추가
        marvel[x][y] = 9
        length += 1
    elif marvel[x][y] == 1:   # 1이면 원래 좌표료 돌아가고 다음 방향으로 변경
        x -= dx[direct[count]]
        y -= dy[direct[count]]
        count += 1

    if count == N:   # count가 배열의 끝까지 간 상태에서 +1을 하면 종료
        break

print(length)


