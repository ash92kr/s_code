import sys
sys.stdin = open("장군_input.txt")


def delta(x, y):

    global count, R2, C2

    dx = [2, 2, -2, -2, 3, 3, -3, -3]
    dy = [3, -3, 3, -3, 2, -2, 2, -2]

    wall = [[[0, 1], [1, 2]], [[0, -1], [1, -2]], [[0, 1], [-1, 2]], [[0, -1], [-1, -2]],
            [[1, 0], [2, 1]], [[1, 0], [2, -1]], [[-1, 0], [-2, 1]], [[-1, 0], [-2, -1]]]

    queue = []
    queue.append((x, y, count))

    while queue:
        x, y, count = queue.pop(0)
        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            flag = 0

            for j in range(len(wall[i])):
                if R2 == x + wall[i][j][0] and C2 == y + wall[i][j][1]:
                    flag = 1

            if flag:
                continue
            if new_x < 0 or new_x >= 10 or new_y < 0 or new_y >= 9:
                continue
            if pan[new_x][new_y] == 1:
                continue
            if new_x == R2 and new_y == C2:
                return count + 1
            pan[new_x][new_y] = 1
            queue.append((new_x, new_y, count+1))

    return -1


R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())

pan = [[0 for _ in range(9)] for _ in range(10)]

count = 0

print(delta(R1, C1))


