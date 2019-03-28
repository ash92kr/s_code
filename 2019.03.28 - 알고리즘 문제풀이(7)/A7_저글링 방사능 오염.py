import sys
sys.stdin = open("A7_저글링 방사능 오염_input.txt")

def BFS(x, y):

    queue = []
    dx = [-1, 1, 0, 0]  # 상/하/좌/우
    dy = [0, 0, -1, 1]
    queue.append((x, y, 3))
    data[x][y] = 0  # 방문 표시

    while queue:
        x, y, time = queue.pop(0)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= r or new_y < 0 or new_y >= c:
                continue
            if data[new_x][new_y] == 1:   # 저글링이면
                queue.append((new_x, new_y, time+1))
                data[new_x][new_y] = 0   # 방문 표시

    return time   # 큐가 비었다면 빈 상태로 표시

# main---------------------
c, r = map(int, input().split())
data = [list(map(int, input())) for _ in range(r)]
start_y, start_x = map(int, input().split())

print(BFS(start_x-1, start_y-1))

remain = 0

for i in range(r):
    for j in range(c):
        if data[i][j] == 1:
            remain += 1

print(remain)
