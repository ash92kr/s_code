import sys
sys.stdin = open("재미있는 오셀로 게임_input.txt")

def iswall(x, y):   # 가장자리 처리

    global N, board

    if x < 1 or x > N:
        return False
    if y < 1 or y > N:
        return False
    if board[x][y] == 0:   # 0이면 벽 + 아직 놓지 않은 곳으로 인식
        return False
    return True


def delta(x, y, player):

    global board

    board[x][y] = player   # 우선 좌표에 해당하는 지점에 돌을 놓음

    dx = [-1, 1, 0, 0, -1, 1, -1, 1]  # 상/하/좌/우/좌상/우상/좌하/우하 순으로 탐색
    dy = [0, 0, -1, 1, -1, -1, 1, 1]

    for i in range(8):

        new_x = x + dx[i]  # 한 방향씩 탐색
        new_y = y + dy[i]
        count = 0

        if iswall(new_x, new_y) == True and board[new_x][new_y] != player:   # 벽이 아닌 상태로 상대방의 돌을 만나면

                while True:

                    new_x += dx[i]   # 바꾼 좌표를 유지하면서 해당 방향으로 계속 나아감
                    new_y += dy[i]
                    count += 1   # 상대방의 돌을 만난 횟수

                    if iswall(new_x, new_y) == True and board[new_x][new_y] == player:   # 벽 전에 내 돌을 만난 경우 상대방 돌을 내 돌로 바꿈
                        for j in range(count):   # 위의 count 횟수만큼 반복해서 처리
                            new_x -= dx[i]   # 내 돌의 위치에서 온 방향만큼 거꾸로 이동하면서
                            new_y -= dy[i]
                            board[new_x][new_y] = player   # 상대방 돌을 내 돌로 바꿈
                        break   # 해당 행위가 끝나면 다른 방향으로 탐색

                    if iswall(new_x, new_y) == False:   # 그런데 내 돌을 만나지 못하면 상대방 돌을 내 돌로 바꾸지 않음
                        break

    # for i in range(len(board)):
    #     print(i, board[i])



T = int(input())

for tc in range(T):

    N, M = map(int, input().split())  # N = 한 변의 길이, M = 돌을 놓는 횟수

    data = []

    for i in range(M):
        data.append(list(map(int, input().split())))

    board = [[0 for _ in range(N+2)] for _ in range(N+2)]   # 가장자리 두르기

    for i in range(2):
        board[(N//2)+i][(N//2)+i] = 2   # 게임 시작을 위한 2(백돌) 놓기

    board[(N//2)][(N//2)+1] = 1   # 게임 시작을 위한 1(흑돌) 놓기
    board[(N//2)+1][(N//2)] = 1

    black = 0
    white = 0

    for i in range(M):
        delta(data[i][1], data[i][0], data[i][2])  # 돌을 놓을 x, y좌표(문제를 잘 읽어보면 좌표가 다름), player

    for i in range(len(board)):   # 마지막 돌을 놓은 다음에 행렬을 순회하면서 1과 2를 셈(그냥 세면 0도 else로 세므로 주의)
        for j in range(len(board)):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print("#{} {} {}".format(tc+1, black, white))
