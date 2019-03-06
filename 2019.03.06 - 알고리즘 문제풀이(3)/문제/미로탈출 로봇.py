import sys
sys.stdin = open("미로탈출 로봇_input.txt")

def delta(x, y):

    global arrow, length, count

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while True:

        # 1은 아래, 2는 왼쪽, 3은 위, 4는 오른쪽
        x += dx[arrow[count]]
        y += dy[arrow[count]]
        print(x, y)

        # if (x > 0 and x < N) and (y > 0 and y < N):
        if maze[x][y] == 0:
            maze[x][y] = 9
            length += 1
        elif maze[x][y] == 1:
            x -= dx[arrow[count]]
            y -= dy[arrow[count]]
            count += 1
            if count == 4:
                count = 0
        else:
            break

    return length


N = int(input())

maze = []

for i in range(N):
    maze.append(list(map(int, input())))

arrow = list(map(int, input().split()))  # 방향의 순서를 가리키는 배열

length = 0
start_x = 0
start_y = 0
count = 0

print(delta(start_x, start_y))
