import sys
sys.stdin = open("D5_미로탈출_input.txt")


def BFS(x, y):

    queue = []
    queue.append((x, y, 3, 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[3][x][y] = 1

    while queue:

        x, y, bomb, count = queue.pop(0)

        for i in range(4):

            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= R or new_y < 0 or new_y >= C:
                continue
            if maze[new_x][new_y] == 1:
                continue
            if maze[new_x][new_y] == 4:
                return count + 1
            if maze[new_x][new_y] == 2 and visited[bomb][new_x][new_y] == 0:
                if bomb > 0:
                    visited[bomb-1][new_x][new_y] = 1
                    queue.append((new_x, new_y, bomb-1, count+1))
                else:
                    continue
            if maze[new_x][new_y] == 0 and visited[bomb][new_x][new_y] == 0:  # 이렇게 0도 조건을 넣는 것이 좋을 때가 있다
                visited[bomb][new_x][new_y] = 1
                queue.append((new_x, new_y, bomb, count+1))

        print(queue)

    return -1


# 폭탄을 사용하지 않았더라도 그 자리는 나중에 다시 도전할 수 있다
# 자외선처럼 폭탄을 사용한 개수를 기록(memoization) or 로봇처럼 visited를 만들어 사용
# 폭탄을 사용한 여부에 대한 visited 체크
# 도착한 이후 return을 하는 방법(count+1)

R, C = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(R)]

visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(4)]

# for i in range(4):
#     print(visited[i])

for i in range(R):
    for j in range(C):
        if maze[i][j] == 3:
            print(BFS(i, j))

