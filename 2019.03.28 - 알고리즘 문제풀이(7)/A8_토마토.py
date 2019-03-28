import sys
sys.stdin = open("토마토_input.txt")

def BFS():

    global r, c

    queue = []
    dx = [-1, 1, 0, 0]  # 상/하/좌/우
    dy = [0, 0, -1, 1]

    zero = 0   # 0의 개수를 담는 변수
    day = 0, 0, 0

    for i in range(r):
        for j in range(c):
            if data[i][j] == 1:
                queue.append((i, j, 0))   # 익은 토마토 자리를 모두 시작점으로 큐에 저장
            elif data[i][j] == 0:    # 0의 개수 카운트
                zero += 1

    if zero == 0:
        return 0   # 토마톼 모두 익은 상태라면 0을 리턴

    while queue:
        x, y, day = queue.pop(0)   # 큐에서 데이터 읽기(현재 좌표)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= r or new_y < 0 or new_y >= c:   # 맵의 범위를 벗어나면 스킵
                continue
            if data[new_x][new_y] == 0:   # 익지 않은 토마토라면
                queue.append((new_x, new_y, day+1))   # 날짜에 + 1을 갱신하는 것이 아니다(토마토마다 +1을 하는 것이 아님
                data[new_x][new_y] = 1   # 방문 표시
                zero -= 1   # 익히면서 차감한다

    if zero == 0:
        return day   # 큐가 빈 상태
    else:
        return -1   # 모든 토마토를 익히지 못한 상태


c, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(r)]

print(BFS())
