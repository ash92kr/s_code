import sys
sys.stdin = open("B1_단지 번호붙이기_input.txt")

def DFS(x, y):

    global N

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # if x < 0 or x >= N or y < 0 or y >= N:
    #     return
    # if data[x][y] != 1:
    #     return

    data[x][y] = 0
    house += 1

    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]
        if 0 < new_x < N or 0 < new_y < N:
            continue
        if data[new_x][new_y] == 1:
            DFS(new_x, new_y)


N = int(input())

data = [list(map(int, input())) for _ in range(N)]

count = []

house = 0



