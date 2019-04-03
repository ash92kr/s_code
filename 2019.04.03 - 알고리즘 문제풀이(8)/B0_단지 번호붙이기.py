import sys
sys.stdin = open("B0_단지 번호붙이기_input.txt")

def DFS(x, y):

    global count

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = 1
    jido[x][y] = 0

    for i in range(4):

        new_x = x + dx[i]
        new_y = y + dy[i]

        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
            continue
        if visited[new_x][new_y] == 1:
            continue
        if jido[new_x][new_y] == 0:
            continue
        visited[new_x][new_y] = 1
        count += 1
        DFS(new_x, new_y)

    return count


N = int(input())

jido = [list(map(int, input())) for _ in range(N)]

visited = [[0 for _ in range(N)] for _ in range(N)]

danji = []


for i in range(N):
    for j in range(N):
        count = 1
        if jido[i][j] != 0:
            danji.append(DFS(i, j))

danji.sort()  # 각 단지에 속하는 집의 수를 오름차순으로 정렬하기

print(len(danji))
for i in range(len(danji)):
    print(danji[i])
