import sys
sys.stdin = open("D4_로봇_input.txt")

# Go 1, 2, 3 -> 각각 명령 1번(진행 방향에서 좌표만 바뀜)
# Turn left, Turn right  -> 가던 방향에서 도는 것
# 위 5가지 명령이 모두 하나의 행동이다

def BFS(x, y, d):

    global end_x, end_y, end_d

    queue = []
    queue.append((x, y, d, 0))

    # 정보 테이블
    dx = [0, 0, 0, 1, -1]  # 동/서/남/북(0, 1), (0, -1)
    dy = [0, 1, -1, 0, 0]

    turn = [[0, 0], [4, 3], [3, 4], [1, 2], [2, 1]]  # 각 방향 전환 시 변화

    visited[d][x][y] = 1  # 현재 위치 visited 체크

    # 현재 위치에서 할 수 있는 모든 명령(5가지)을 하고 다음 단계로 넘어간다
    # 현재 위치의 방향도 갈 수 있는 변수 + 명령 횟수도 변수로 포함한다
    while queue:

        x, y, d, count = queue.pop(0)

        if x == end_x-1 and y == end_y-1 and d == end_d:
            return count

        # Go 1, 2, 3를 가능한 만큼 큐에 넣기
        # Go 1에는 벽이 있으나, Go 2는 벽이 없는 경우 -> 벽이 있으면 그 이후의 동작은 break
        # Go 1은 지나간 적이 있으나, Go 2/3는 지나갈 수 있다
        for i in range(1, 4):
            new_x = x + (dx[d]*i)
            new_y = y + (dy[d]*i)

            # 맵의 범위 체크
            if new_x < 0 or new_x >= M or new_y < 0 or new_y >= N:
                break  # Go 1, 2가 나가면 Go 3을 할 필요 없다
            if factory[new_x][new_y] == 1:
                break  # 벽이 있으면 그 이후 동작은 할 필요가 없다
            if visited[d][new_x][new_y] == 1:
                continue

            visited[d][new_x][new_y] = 1
            queue.append((new_x, new_y, d, count+1))

        # Turn left, Turn Right을 가능한 만큼 큐에 넣기
        # 단, 같은 자리를 여러 번 지나가야 하나, 방향이 다르면 다른 것으로 인식
        # 2차원 맵을 4개를 만들어도 되지만, 3차원 배열 1개가 더 편하다
        # 방향 바꾸기를 할 때는 벽 체크나 범위 체크가 필요없다
        for i in range(2):

            new_d = turn[d][i]   # i가 0이면 왼쪽 turn, 1이면 오른쪽 turn

            if visited[new_d][x][y] == 1:  # 면/행/열 순으로 넣어야 한다
                continue

            visited[new_d][x][y] = 1
            queue.append((x, y, new_d, count+1))

        # print(queue)



M, N = map(int, input().split())   # M = 직사각형 세로 길이, N = 직사각형 가로 길이

factory = [list(map(int, input().split())) for _ in range(M)]

start_x, start_y, start_d = map(int, input().split())

end_x, end_y, end_d = map(int, input().split())

# 3차원 배열(열/행/면 순)
visited = [[[0 for _ in range(N)] for _ in range(M)] for _ in range(5)]

# for i in range(5):
#     print(i, visited[i])

print(BFS(start_x-1, start_y-1, start_d))


# 1시간 문제 이해
# 1시간 코드 짜기
# 1시간 디버깅