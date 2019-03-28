import sys
sys.stdin = open("C2_장기_input.txt")

def BFS(x, y):

    global N, M, S, K

    queue = []
    queue.append((x, y, 0))
    pan[x][y] = 1   # visited 체크

    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]   # 장애물 처리 주의

    while queue:
        x, y, count = queue.pop(0)

        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= M or new_y < 0 or new_y >= N:
                continue
            if new_x == (K-1) and new_y == (S-1):
                return count + 1
            if pan[new_x][new_y] == 1:   # 가지치기!!! 
                continue
            pan[new_x][new_y] = 1   # visited 체크
            queue.append((new_x, new_y, count+1))

    return -1



N, M = map(int, input().split())  # M = 행, N = 열

R, C, S, K = map(int, input().split())   # C = 행, R = 열, K = 행, S = 열

pan = [[0 for _ in range(N)] for _ in range(M)]   # 열이 안쪽, 행이 바깥쪽

print(BFS(C-1, R-1))