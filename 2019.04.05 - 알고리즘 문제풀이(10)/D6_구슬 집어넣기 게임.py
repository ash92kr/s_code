import sys
sys.stdin = open("D6_구슬 집어넣기 게임_input.txt")


def BFS(rx, ry, bx, by):

    queue_r = []
    queue_r.append((rx, ry, 0))

    queue_b = []
    queue_b.append((bx, by, 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue_r:

        rx, ry, count_r = queue_r.pop(0)
        bx, by, count_b = queue_b.pop(0)

        if count_r > 10:  # 기울임 횟수가 10회보다 크면 실패
            return -1

        for i in range(4):

            new_rx = rx + dx[i]
            new_ry = ry + dy[i]

            new_bx = bx + dx[i]
            new_by = by + dy[i]

            # 이동 방향에 벽이 있는 구슬은 움직일 수 없다
            # 빨간 구슬과 파란 구슬이 같은 위치로 움직이는 경우 실패
            # 파란구슬이 목표 구멍으로 들어가면 실패
            # 빨간구슬이 목표 구멍으로 들어가야 성공
            if new_rx < 0 or new_rx >= R or new_ry < 0 or new_ry >= C:
                continue
            if new_bx < 0 or new_bx >= R or new_by < 0 or new_by >= C:
                continue
            # 파란 구슬과 빨간 구슬이 같은 위치면 패스
            if new_rx == new_bx and new_ry == new_by and count_r == count_b:
                continue
            if maze[new_rx][new_ry] == '#':  # 벽일 경우 원래 좌표로 놓고 나머지 조건 체크한다
                new_rx, new_ry = rx, ry
            if maze[new_bx][new_by] == '#':
                new_bx, new_by = bx, by
            
            if visited[new_rx][new_ry][new_bx][new_by] == 1:
                continue
            # 파란 구슬이 목표 구멍이면 패스
            if maze[new_bx][new_by] == 'H':
                continue
            # 빨간 구슬이 목표 구멍이면 성공 리턴
            if maze[new_rx][new_ry] == 'H' and maze[new_bx][new_by] != 'H':
                return count_r + 1

            # 최단 거리를 구하기 위해 두 구슬의 각 좌표를 visited에 체크함(중복 방문 방지)
            visited[new_rx][new_ry][new_bx][new_by] = 1
            queue_r.append((new_rx, new_ry, count_r+1))
            queue_b.append((new_bx, new_by, count_b+1))

        # print(queue_b)
        # print(queue_r)

    return -1


# 두 구슬은 동일한만큼 움직인다
# 우선 간 다음에 갈 수 없다면 좌표를 원래대로 되돌린다
# continue는 큐에 넣지 않는 경우이다

T = int(input())

for tc in range(T):

    R, C = map(int, input().split())

    maze = [list(map(str, input())) for _ in range(R)]

    # 두 개 구슬의 좌표에 대한 각 상황을 체크해야 하므로 4차원 check 배열이 필요하다
    # 하나의 구슬이 어떤 점을 방문했을 때, 다른 구슬이 지나갔는지 확인
    # 어떤 구슬을 먼저 사용할지는 상관없다
    
    visited = [[[[0 for _ in range(C)] for _ in range(R)] for _ in range(C)] for _ in range(R)]

    start_rx = 0
    start_ry = 0
    start_bx = 0
    start_by = 0

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'R':
                start_rx = i
                start_ry = j
            if maze[i][j] == 'B':
                start_bx = i
                start_by = j

    print(BFS(start_rx, start_ry, start_bx, start_by))
