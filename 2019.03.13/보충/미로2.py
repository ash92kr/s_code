# BFS는 큐를 만들어야 한다

# Q.append((x, y))   # 튜플로 집어 넣음 -> 이게 싫으면 x, y 좌표별로 스택을 다르게 만듦
# visited[x][y] = 1
# while Q:   =   while len(Q) != 0:
#     x, y = Q.pop(0)
#     벽처리 통과
#     4방향 돌려서 갈 수 있는 부분 체크하기
#     3을 만나면 끝
#     Q.append()
#     visited
# return 0

import sys
sys.stdin = open("미로2_input.txt")


# def iswall(x, y):
#
#     if x < 0 or x >= 100:
#         return False
#     if y < 0 or y >= 100:
#         return False
#     if visited[x][y] == 1:
#         return False
#     return True


def BFS(x, y):

    global maze, visited

    Queue = []   # BFS는 큐를 만든 다음에 바로 하나를 넣는다
    Queue.append((x, y))
    visited[x][y] = 1   # 출발점도 visited처리

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while Queue:   # 큐가 하나라도 있으면 처리
        x, y = Queue.pop(0)   # 첫 번째 출발점을 빼낸 다음
        visited[x][y] = 1

        for i in range(4):   # 같은 델타 방식

            # if iswall(x+dx[i], y+dy[i]) == True:
            new_x = x + dx[i]
            new_y = y + dy[i]

            if maze[new_x][new_y] == 1:   # 이 미로에서는 가장자리가 모두 벽으로 막혀 있음(데이터 확인) = 벽처리 함수 필요 없음
                continue
            if visited[new_x][new_y] == 1:   # 방문한 적이 있으면 pass
                continue
            if maze[new_x][new_y] == 0:   # 길인 지점은 그 곳의 좌표를 큐에 넣고 방문처리함 -> 방문 순서는 거리가 같은 곳의 상/하/좌/우 순으로 실시
                Queue.append((new_x, new_y))
                visited[new_x][new_y] = 1
            if maze[new_x][new_y] == 3:   # 도착점에 도달하면 종료
                return 1

    return 0


def find_start(maze):

    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                return i, j   # i, j를 x, y에 바로 넣을 수 있다

for tc in range(10):

    N = int(input())

    maze = []

    for i in range(100):
        maze.append(list(map(int, input())))

    visited = [[0 for _ in range(100)] for _ in range(100)]   # 한번 갔던 곳을 다시 가는 곳을 막기 위해 visited처리

    # maze = [[int(x) for x in input()] for _ in range(100)]

    # for i in range(len(maze)):
    #     print(i, maze[i])

    start_x, start_y = find_start(maze)  # 출발점 찾기 - 함수로 처리

    print("#{} {}".format(N, BFS(start_x, start_y)))
