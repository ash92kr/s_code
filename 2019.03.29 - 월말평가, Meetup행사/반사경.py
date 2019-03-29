import sys
sys.stdin = open("반사경_input.txt")

def DFS(x, y, idx):   # 달팽이와 비슷한 문항

    global mirror

    dx = [0, -1, 1, 0]   # 우 / 상 / 하 / 좌
    dy = [1, 0, 0, -1]   # 우 / 하 / 좌/ 상으로 하면 편하다

    new_x = x + dx[idx]   # 그냥 x, y로 계속 돌려도 된다
    new_y = y + dy[idx]

    while True:

        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
            return mirror
        if data[new_x][new_y] == 1:
            mirror += 1
            if idx % 2 == 0:
                idx += 1
            else:
                idx -= 1
            # DFS(x, y, idx)
        if data[new_x][new_y] == 2:
            mirror += 1
            if idx < 2:
                idx += 2
            else:
                idx -= 2
            # DFS(x, y, idx)

        new_x += dx[idx]   # 무조건 한 칸씩 이동한다
        new_y += dy[idx]


T = int(input())

for tc in range(T):

    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    mirror = 0

    idx = 0

    print("#{} {}".format(tc+1, DFS(0, 0, 0)))  # 방향 전환이므로 DFS가 아님


