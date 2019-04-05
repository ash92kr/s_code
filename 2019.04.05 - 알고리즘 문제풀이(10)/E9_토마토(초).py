import sys
sys.stdin = open("E9_토마토(초)_input.txt")

def BFS():

    global M, N, H

    zero = 0
    day = 0
    queue = []

    for k in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[k][i][j] == 1:
                    queue.append((i, j, k, 0))
                    visited[k][i][j] = 1
                elif tomato[k][i][j] == 0:
                    zero += 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dh = [-1, 1]

    if zero == 0:
        return 0

    while queue:

        x, y, h, day = queue.pop(0)

        for i in range(4):

            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue
            if tomato[h][new_x][new_y] == -1 or tomato[h][new_x][new_y] == 1:
                continue
            if visited[h][new_x][new_y] == 1:
                continue

            tomato[h][new_x][new_y] = 1
            visited[h][new_x][new_y] = 1
            queue.append((new_x, new_y, h, day+1))
            zero -= 1

        for i in range(2):

            new_h = h + dh[i]

            if new_h < 0 or new_h >= H:
                continue
            if tomato[new_h][x][y] == -1 or tomato[new_h][x][y] == 1:
                continue
            if visited[new_h][x][y] == 1:
                continue

            tomato[new_h][x][y] = 1
            visited[new_h][x][y] = 1
            queue.append((x, y, new_h, day+1))
            zero -= 1

    if zero == 0:
        return day
    else:
        return -1


M, N, H = map(int, input().split())  # M = 열, N = 행, H = 높이

tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# print(tomato)

# for i in range(H):
#     print(tomato[i])

visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

# print(visited)

# 정수 1 = 익은 토마트, 0 = 익지 않은 토마트, -1 = 토마토 없음

print(BFS())



