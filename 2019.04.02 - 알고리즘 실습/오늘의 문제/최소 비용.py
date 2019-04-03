import sys
sys.stdin = open("최소 비용_input.txt")

def BFS(x, y):

    global N

    # D = [[999999 for _ in range(N)] for _ in range(N)]
    # D[0][0] = 0
    # Q = [(0, 0)]

    # while Q:
    #     r, c = Q.pop(0)
    #     for i in range(4):
    #         tr, tc = r + dr[i], c + dc[i]
    #         if 0 <= tr < N and 0 <= tc < N:
    #             diff = 0
    #             if arr[tr][tc] > arr[r][c]:
    #                 diff = arr[tr][tc] - arr[r][c]
    #             if D[tr][tc] > D[r][c] + diff + 1:
    #                 D[tr][tc] = D[r][c] + diff + 1
    #                 Q.append((tr, tc))
    #
    #     print("#{} {}".format(tc + 1, D[N - 1][N - 1]))


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
            # if visit[new_x][new_y] == 1:
            #     continue
            # if new_x == N-1 and new_y == N-1:
            #     if data[x][y] < data[new_x][new_y]:
            #         count += (data[new_x][new_y] - data[x][y])
            #     else:
            #         count += 1
            #     if min_count > count:
            #         min_count = count
            #
            # if data[x][y] < data[new_x][new_y]:
            #     queue.append((new_x, new_y, count+(data[new_x][new_y]-data[x][y])))
            # elif data[x][y] == data[new_x][new_y]:
            #     queue.append((new_x, new_y, count+1))
            # else:
            #     queue.append((new_x, new_y, count+1))

            # visit[new_x][new_y] = 1


T = int(input())

for tc in range(T):

    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    # print(data)
    # min_count = 987654321

    print("#{} {}".format(tc+1, BFS(0, 0)))


