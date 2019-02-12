import sys
sys.stdin = open("input.txt")

# 사다리 타기 - 2에 도착하려면 어떤 지점에서 출발해야 하는가?

for tc in range(10):

    N = int(input())   # 테스트 케이스 번호
    ladder = [ list(map(int, input().split())) for _ in range(100)]   # 2차원 배열로 원소 넣기

    start_x = 99  # 출발점 좌표 초기화(x는 99행)
    start_y = 0

    for i in range(len(ladder)):
        for j in range(len(ladder[0])):
            if ladder[i][j] == 2:
                start_y = j

    temp = start_y   # 기준 y좌표

    while start_x > 0:   # 도착점 좌표(x가 0행이 되면 끝)

        if ladder[start_x-1][start_y] == 1:   # 바로 위쪽이 1인 경우
            if start_y > 0 and ladder[start_x-1][start_y-1] == 1:    # y좌표가 0열보다 크고 좌측으로 1이 나온 경우
                start_x -= 1
                start_y -= 1
            elif start_y < 99 and ladder[start_x-1][start_y+1] == 1:   # y좌표가 99열보다 작고 우측으로 1이 나온 경우
                start_x -= 1
                start_y += 1
            else:   # y 좌표가 0열, 99열인 경우와 현재 좌표에서 좌우가 1이 아닌 경우
                start_x -= 1
                temp = start_y   # 기준열을 바꿈(좌우로 사다리를 이동한 경우 기준열을 바꿔야 한다)
        else:    # 바로 위쪽이 0인 경우
            if temp > start_y and ladder[start_x][start_y-1] == 1:   # 기준열이 y좌표보다 큰 경우 좌측으로 이동
                start_y -= 1
            elif temp < start_y and ladder[start_x][start_y+1] == 1:   # 기준열이 y좌표보다 작은 경우 우측으로 이동
                start_y += 1

    print(f'#{N} {start_y}')


