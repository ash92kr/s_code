def maze(y, x):
    global N, flag
    dx = [0, 0, -1, 1]   # 먼저 좌/우부터 확인한 다음에 상/하로 이동한다
    dy = [-1, 1, 0, 0]

    data[y][x] = 9 #방문표시

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny == N: continue   # 벽처리
        if nx < 0 or nx == N: continue
        if data[ny][nx] == 9 : continue   # visited 처리
        if data[ny][nx] == 1 : continue   # 벽처리
        if data[ny][nx] == 3:   # 끝나는 지점
            flag = 1
            return   # 모든 갈 수 있는 곳을 다 방문한 다음에 돌아온다
        maze(ny, nx)   # 재귀로 스택에 쌓다가 더 이상 갈 수 없으면 return한다 -> 다시 갈 수 있는 방향까지 되돌아 간다
# 함수를 완전히 비워야 프로그램이 종료된다

def findStart(data):
    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                return y, x

import sys
sys.stdin = open('미로1_input.txt', 'r')
T = 10
N = 16
for tc in range(T):
    flag = 0   # flag 변수를 return하기
    no = int(input())
    data = [[int(x) for x in input()] for _ in range(N)]  # 미로를 중첩리스트로 저장
    visit = [[0 for _ in range(N)] for _ in range(N)]

    sy, sx = findStart(data)
    maze(sy, sx)   # DFS
    print("#{} {}".format(tc+1, flag))