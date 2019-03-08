import sys
sys.stdin = open("사다리2_input.txt")

def iswall(x, y):

    global ladder

    if x < 0 or x >= 100:
        return False
    if y < 0 or y >= 100:
        return False
    if ladder[x][y] == 0 or ladder[x][y] == 9:
        return False
    return True

def maze(x, y):

    global min_count, ladder

    dx = [0, 0, 1]   # 좌, 우, 하
    dy = [-1, 1, 0]   # 먼저 좌, 우부터 살피고 아래로 내려간다

    for i in range(len(ladder[0])):

        if ladder[0][i] == 1:

            count = 0
            visited = [[0 for _ in range(100)] for _ in range(100)]

            while x < 100:

                for j in range(3):
                    new_x = x + dx[j]
                    new_y = ladder[x][i] + dy[j]
                    if iswall(new_x, new_y) == True:
                        visited[new_x][new_y] = 9
                        count += 1

            if min_count >= count:
                min_count = i

    return min_count


T = int(input())

for tc in range(T):

    ladder = []

    for i in range(100):
        ladder.append(list(map(int, input().split())))

    # for i in range(100):
    #     print(i, ladder[i])

    # start_x = 0
    # start_y = 0
    min_count = 9999

    for i in range(100):
        if ladder[0][i] == 1:
            maze()


    print("#{} {}".format(tc+1, min_count))

