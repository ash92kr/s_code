import sys
sys.stdin = open("D5_미로탈출_input.txt")

# 폭탄의 개수 정보를 가지고 다녀야 한다(3차원 배열) - 같은 자리를 계속 지나다녀야 한다

def BFS(x, y):

    global r, c

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = []
    queue.append((x, y, 0))
    visited[x][y] = 1

    bomb = 3

    while queue:

        x, y, count = queue.pop(0)

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 1 or new_x >= r or new_y < 1 or new_y >= c:
                continue
            if maze[new_x][new_y] == 1:
                continue
            if maze[new_x][new_y] == 2:
                if bomb > 0:
                    bomb -= 1
                    visited[new_x][new_y] = 1
                else:
                    continue
            if maze[new_x][new_y] == 4:
                return count + 1
            if visited[new_x][new_y] == 1:
                continue
            visited[new_x][new_y] = 1
            queue.append((x, y, count+1))

    return -1



# def DFS(x, y, bomb):
#
#     global r, c, count, flag
#
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     visited[x][y] = 1
#
#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]
#
#         # if new_x < 1 or new_x >= r or new_y < 1 or new_y >= c:
#         #     continue
#         if maze[new_x][new_y] == 1:
#             continue
#         if maze[new_x][new_y] == 2:
#             if bomb > 0:
#                 bomb -= 1
#             else:
#                 continue
#         if maze[new_x][new_y] == 4:
#             flag = 1
#             return count + 1
#         if visited[new_x][new_y] == 1:
#             continue
#         visited[new_x][new_y] = 1
#         count += 1
#         DFS(new_x, new_y, bomb)



r, c = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(r)]

start_x, start_y = 0, 0

for i in range(r):
    for j in range(c):
        if maze[i][j] == 3:
            start_x = i
            start_y = j

visited = [[0 for _ in range(c)] for _ in range(r)]

print(BFS(start_x, start_y))

# bomb = 3
# count = 0
# flag = 0
#
# DFS(start_x, start_y, bomb)
#
# if flag:
#     print(count)
# else:
#     print(-1)
