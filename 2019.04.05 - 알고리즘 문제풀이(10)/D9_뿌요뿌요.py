import sys
sys.stdin = open("D9_뿌요뿌요_input.txt")


# def update(i, j):
#
#     temp = []
#
#     for k in range(6):
#         temp = ['.'] * 12
#         for l in range(12):
#             temp[11-l] = puyo[l][k]
#         # print(temp)
#
#         idx = 0
#         c_count = 0
#
#         while c_count < 12:
#
#             if temp[idx] == '.':
#                 temp.pop(idx)
#                 temp.append('.')
#             else:
#                 idx += 1
#
#             c_count += 1
#
#         for m in range(12):
#             puyo[m][k] = temp[m]
#

# def remove(x, y, temp):
#
#     queue = []
#     queue.append((x, y))
#
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     visited = [[0 for _ in range(6)] for _ in range(12)]
#     visited[x][y] = 1
#     puyo[x][y] = '.'
#
#     while queue:
#
#         x, y = queue.pop(0)
#
#         for i in range(4):
#
#             new_x = x + dx[i]
#             new_y = y + dy[i]
#
#             if new_x < 0 or new_x >= 12 or new_y < 0 or new_y >= 6:
#                 continue
#             if puyo[new_x][new_y] != temp:
#                 continue
#             if visited[new_x][new_y] == 1:
#                 continue
#
#             queue.append((new_x, new_y))
#             visited[new_x][new_y] = 1
#             puyo[new_x][new_y] = '.'


def update():

    for i in range(6):
        temp = []
        for j in range(12):   # 열 방향 돌리는 방법 알아두기
            if puyo[11-j][i] != '.':
                temp.append(puyo[11-j][i])
                puyo[11-j][i] = '.'

        # print(temp)

        if len(temp) > 0:
            for k in range(len(temp)):
                puyo[11-k][i] = temp[k]   # 다시 원래 행에 두기


def BFS(x, y, temp):

    global flag

    queue = []
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[0 for _ in range(6)] for _ in range(12)]
    visited[x][y] = 1

    # count = 1
    location = [(x, y)]

    while queue:

        x, y = queue.pop(0)

        for i in range(4):

            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= 12 or new_y < 0 or new_y >= 6:
                continue
            if puyo[new_x][new_y] != temp or puyo[new_x][new_y] == '.':
                continue
            if visited[new_x][new_y] == 1:
                continue

            # count += 1
            queue.append((new_x, new_y))
            location.append((new_x, new_y))
            visited[new_x][new_y] = 1

    # if count >= 4:
    #     return True
    # else:
    #     return False

    if len(location) >= 4:
        for i in range(len(location)):
            puyo[location[i][0]][location[i][1]] = '.'
        flag = 1


# 위에서 아래로 내려가므로 11행을 0행에 넣어도 된다
# 이런 문제가 아이디어 문제

# 우선 4개가 모여있는지 확인하자 - (11, 0)부터 for문을 돌려야 한다
# BFS로 상하좌우에 같은 값이 있는지 확인
# 그러나 상하좌우 탐색과 동시에 .으로 바꾸는 것은 불가능하다

# 4개 이상인 좌표는 리스트에 넣고 .으로 바꾼다 - 여기까지가 함수 1개
# .으로 바꾼 것들을 떨어뜨림으로써 1사이클

# 중력으로 떨어뜨리는 경우는 열을 for문으로 돌려서 확인해야 한다(열 고정, 행을 아래에서 위로)
# 문자를 만나면 스택에 옮기고 모든 열의 행을 .으로 바꾼다


T = int(input())

for tc in range(T):

    puyo = [list(map(str, input())) for _ in range(12)]

    # for i in range(12):
    #     print(puyo[i])

    # start_x = 11
    # start_y = 0

    count = 0

    # for i in range(11, -1, -1):
    #     for j in range(6):
    #         flag = 0
    #         if puyo[i][j] != '.':
    #             flag = BFS(i, j, puyo[i][j])
    #         if flag:
    #             remove(i, j, puyo[i][j])
    #             update(i, j)
    #             count += 1

    # flag = 0

    while True:

        flag = 0

        for i in range(11, -1, -1):
            for j in range(6):
                if puyo[i][j] != '.':
                    BFS(i, j, puyo[i][j])   # remove를 포함함
            # print(i, puyo[i])

        update()

        if flag:
            count += 1
        else:
            break

    # for i in range(11, -1, -1):
    #     print(puyo[i])

    print(count)