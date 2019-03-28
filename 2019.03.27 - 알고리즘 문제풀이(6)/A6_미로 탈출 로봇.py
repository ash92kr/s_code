import sys
sys.stdin = open("A6_미로 탈출 로봇_input.txt")

def BFS(x, y):

    global r, c, end_x, end_y

    queue = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue.append((x, y, 0))   # 1) 시작점을 큐에저장(방문표시)
    data[x][y] = 1

    while queue:
        x, y, time = queue.pop(0)   # 2) 큐에서 데이터 읽기(현재좌표)
        if x == end_x - 1 and y == end_y - 1:   # 바깥으로 뺌으로써 마침
            return time
        for i in range(4):   # 3) 사방탐색하면서 연결점(길)을 찾아 큐에저장
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= r or new_y < 0 or new_y >= c:
                continue
            if data[new_x][new_y] == 0:
                queue.append((new_x, new_y, time+1))
                data[new_x][new_y] = 1  # 방문처리 반드시 할 것!!!!

    return -1   # 4) 큐가 빈상태(예외상황)


c, r = map(int, input().split())

start_y, start_x, end_y, end_x = map(int, input().split())

data = [list(map(int, input())) for _ in range(r)]

print(BFS(start_x-1, start_y-1))