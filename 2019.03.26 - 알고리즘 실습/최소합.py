import sys
sys.stdin = open("최소합_input.txt")

def iswall(x, y):  # 벽처리

    global N

    if x < 0 or x >= N:
        return False
    if y < 0 or y >= N:
        return False
    return True


def delta(x, y, temp):

    global hab

    if temp > hab:   # 가지치기
        return

    dx = [0, 1]
    dy = [1, 0]

    if x == N - 1 and y == N - 1:  # x,y 좌표 마무리
        if temp < hab:
            hab = temp
    else:   # 그렇지 않은 경우
        for i in range(2):   # 우하 방향 탐색
            new_x = x + dx[i]
            new_y = y + dy[i]
            if iswall(new_x, new_y) == True:
                delta(new_x, new_y, temp + data[new_x][new_y])   # 여기에 +를 해야 되돌아감


T = int(input())

for tc in range(T):

    N = int(input())

    data = []

    for i in range(N):
        data.append(list(map(int, input().split())))

    start_x = 0
    start_y = 0

    hab = 987654321
    temp = data[start_x][start_y]

    delta(start_x, start_y, temp)

    print("#{} {}".format(tc+1, hab))



