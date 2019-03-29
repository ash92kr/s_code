import sys
sys.stdin = open("장기_복습_input.txt")

def BFS(x, y):

    global N, M, S, K

    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]

    queue = []
    queue.append((x, y, 0))
    pan[x][y] = 1

    while queue:
        x, y, count = queue.pop(0)

        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue
            if pan[new_x][new_y] == 1:
                continue
            if new_x == (S-1) and new_y == (K-1):
                return count + 1

            pan[new_x][new_y] = 1
            queue.append((new_x, new_y, count+1))

    return -1


N, M = map(int, input().split())

R, C, S, K = map(int, input().split())

pan = [[0 for _ in range(M)] for _ in range(N)]

print(BFS(R-1, C-1))


