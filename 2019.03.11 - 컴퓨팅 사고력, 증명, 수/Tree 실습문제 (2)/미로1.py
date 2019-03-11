import sys
sys.stdin = open("미로1_input.txt")

def iswall(x, y):
    global maze

    if x < 0 or x >= len(maze):
        return False
    if y < 0 or y >= len(maze):
        return False
    if maze[x][y] == 1 or visited[x][y] == 1:
        return False
    return True


def delta(x, y):
    global maze, solve

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if iswall(new_x, new_y) == True:
            if maze[new_x][new_y] == 3:
                solve = 1
            visited[new_x][new_y] = 1
            delta(new_x, new_y)


for tc in range(10):

    N = int(input())

    maze = []

    for i in range(16):
        maze.append(list(map(int, input())))

    start_x = 0
    start_y = 0

    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                start_x, start_y = i, j

    visited = [[0 for _ in range(len(maze))] for _ in range(len(maze))]
    visited[start_x][start_y] = 1

    solve = 0
    delta(start_x, start_y)

    print("#{} {}".format(N, solve))