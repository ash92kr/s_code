import sys
sys.stdin = open("보급로_input.txt")

def BFS(x, y):

    queue = []
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[987654321 for _ in range(N)] for _ in range(N)]   # 누적값 배열 처리
    visited[x][y] = 0   # 시작 지점 초기화

    while queue:

        x, y = queue.pop(0)

        for i in range(4):

            new_x = x + dx[i]   # 델타 검색
            new_y = y + dy[i]

            if 0 <= new_x < N and 0 <= new_y < N:   # 벽처리 통과 조건
                if visited[new_x][new_y] > visited[x][y] + data[new_x][new_y]:   # 기존 누적값에다 원래 값을 더한 게 작은 경우
                    visited[new_x][new_y] = visited[x][y] + data[new_x][new_y]   # 누적값 배열에 저장하고 새로운 좌표를 queue에 넣음
                    queue.append((new_x, new_y))

    return visited[N-1][N-1]   # 가장 마지막의 우하단 값 return



T = int(input())

for tc in range(T):

    N = int(input())

    data = [list(map(int, input())) for _ in range(N)]

    print("#{} {}".format(tc+1, BFS(0, 0)))
