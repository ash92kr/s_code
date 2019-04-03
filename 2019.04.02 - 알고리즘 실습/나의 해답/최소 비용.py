import sys
sys.stdin = open("최소 비용_input.txt")

def BFS(x, y):

    global N

    queue = []
    queue.append((x, y))

    # 누적 합계
    n_sum = [[987654321 for _ in range(N)] for _ in range(N)]
    n_sum[x][y] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:

        x, y = queue.pop(0)

        for i in range(4):

            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                continue

            temp = 0

            if data[x][y] < data[new_x][new_y]:
                temp = data[new_x][new_y] - data[x][y]

            if n_sum[new_x][new_y] > n_sum[x][y] + temp + 1:
                n_sum[new_x][new_y] = n_sum[x][y] + temp + 1
                queue.append((new_x, new_y))

    return n_sum[N-1][N-1]


T = int(input())

for tc in range(T):

    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    print("#{} {}".format(tc+1, BFS(0, 0)))
