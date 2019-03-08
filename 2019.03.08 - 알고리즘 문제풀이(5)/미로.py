import sys
sys.stdin = open("미로_input.txt")

def iswall(x, y):

    global data

    if x < 0 or x >= 16:
        return False
    if y < 0 or y >= 16:
        return False
    if data[x][y] == 1:
        return False
    return True

def find_goal(x, y):

    global flag, data

    dx = [-1, 1, 0, 0]   # 상/하/좌/우
    dy = [0, 0, -1, 1]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if iswall(new_x, new_y) == True:
            if data[new_x][new_y] == 3:
                flag = 1
                return flag
            data[new_x][new_y] = 1
            find_goal(new_x, new_y)

    return flag


for tc in range(10):

    N = int(input())

    data = []

    for i in range(16):
        data.append(list(map(int, input())))

    start_x = 0
    start_y = 0
    flag = 0

    for i in range(16):
        for j in range(16):
            if data[i][j] == 2:
                start_x = i
                start_y = j

    data[start_x][start_y] = 9

    find_goal(start_x, start_y)

    print("#{} {}".format(N, flag))