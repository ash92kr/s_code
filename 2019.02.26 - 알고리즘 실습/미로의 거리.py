import sys
sys.stdin = open("미로의 거리_input.txt")

def find_wall(x, y):

    global maze, N

    if x < 0 or x >= N:
        return False
    if y < 0 or y >= N:
        return False
    # if maze[x][y] == 1:   # 이 부분이 빠진 이유 = DFS에서 사용되기 때문
    #     return True   # 한 방향으로만 이동되게 만든다(지그재그 이동 불가)

    return True


def find_maze(x, y):

    global N, maze, visited

    queue = []   # BFS는 큐를 만들고, DFS는 재귀함수를 이용하는 것
    queue.append((x, y))   # x, y 좌표를 튜플로 넣음(enqueue)
    visited[x][y] = 1   # 출발 좌표에는 1을 넣음

    while len(queue) >= 1:

        x, y = queue.pop(0)   # 큐에서 1번째 좌표를 뺌(dequeue)

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        for z in range(4):
            new_x = x + dx[z]
            new_y = y + dy[z]   # 이 부분은 델타 검색과 동일

            if find_wall(new_x, new_y) == True:   # 벽 처리 함수 True여야 벽이 아님
                # 벽이 아닌 부분과 방문하지 않은 지점을 방문한다
                if maze[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
                    visited[new_x][new_y] = visited[x][y] + 1
                    queue.append((new_x, new_y))  # 인접한 좌표 중 갈 수 있는 좌표들을 모두 큐에 넣음
                    # find_maze(new_x, new_y)
                elif maze[new_x][new_y] == 3:  # new_x, new_y가 3이면 끝이므로
                    return visited[x][y] - 1   # 직전 x, y좌표의 visited 값에서 -1(시작점) 처리

    return 0   # 도착점에 닿지 못한 경우


T = int(input())

for tc in range(T):

    N = int(input())

    maze = []   # 미로의 내용 채우기

    for i in range(N):
        maze.append(list(map(int, input())))

    start_x = 0   # 출발 x좌표
    start_y = 0   # 출발 y좌표

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2:
                start_x = i
                start_y = j

    maze[start_x][start_y] = 1   # 출발점은 1로 채우기

    visited = [[0 for _ in range(N)] for _ in range(N)]   # 방문했는지 여부를 표시하는 2차원 배열

    print(f'#{tc+1} {find_maze(start_x, start_y)}')
