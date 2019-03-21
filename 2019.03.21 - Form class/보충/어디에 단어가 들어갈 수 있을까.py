import sys
sys.stdin = open("어디에 단어가 들어갈 수 있을까_input.txt")

T = int(input())

for tc in range(T):

    N, K = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0 for _ in range(N)] for _ in range(N)]  # 방문 처리 필요
    count = 0

    # 가로 방향 검사
    for i in range(N):
        for j in range(N):   # 가로/세로 순회
            check = 0
            if visited[i][j] == 1:   # 방문한 곳은 pass
                continue
            if data[i][j] == 1 and visited[i][j] == 0:   # 공간 있고 방문하지 않았다면
                for k in range(N-j):   # 이 부분이 while문
                    if data[i][j+k] == 1:   # 계속 가면서 visited 체크
                        visited[i][j+k] = 1
                        check += 1  # 공간 개수 체크
                    else:   # 벽을 만나면 바로 종료
                        break
            if check == K:  # check가 K와 같으면 count += 1
                count += 1

    # 세로 방향 검사(i, j만 바꿈)
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):   # j를 바꾸더라도 다음 j를 가지고 돈다
            check = 0        # 따라서 j를 바꾸고 싶으면 while문을 사용해야 한다
            if visited[j][i] == 1:
                continue
            if data[j][i] == 1 and visited[j][i] == 0:  # and는 단축 연산을 한다(앞이 False면 뒤를 실행하지 않음)
                for k in range(N-j):                    # or도 단축 연산 실시(앞이 True면 뒤를 보지 않음)
                    if data[j+k][i] == 1:               
                        visited[j+k][i] = 1
                        check += 1
                    else:
                        break
            if check == K:
                count += 1

    print("#{} {}".format(tc+1, count))

# for
    # for
        # if
            # while