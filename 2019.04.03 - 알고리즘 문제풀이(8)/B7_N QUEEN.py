import sys
sys.stdin = open("B7_N QUEEN_input.txt")

# 우선은 행마다 하나씩 퀸을 놓아보자 - 어디에 놓을 수 있는가?(순열)
# 그 다음에 겹치는지를 체크
# N행에 도달하면 종료된다
# N열에 도달할 때까지 종료된다

# depth = 0행부터 행 개수를 추가한다
# check 함수에 행과 열을 인자로 넣어준다 -> 그러나 n^2만큼 체크하므로 속도 저하 발생
# check 함수로 체크할 대상은 놓을 위치의 위쪽, 왼쪽 대각선, 오른쪽 대각선을 확인하면 된다

# check 개선 방향(전체 2배 길이로 만든다)
# 1차원 배열을 3개를 만들어 어떤 열에 놓았는지 확인(for문 필요 없이 if문으로 체크)
# 직선의 경우 1차원 리스트 N개를 만듦
# 우상향 대각선의 경우 N = 4인 경우 7개 리스트로 만들어서 체크(행+열 인덱스를 더하면 1차원 배열의 인덱스가 나옴)
# 좌상향 대각선도 7개 리스트로 만들어서 열에 놓았는지 체크((N-1)-(r-c))의 규칙

# 말을 놓고 check를 한 다음에, 모두 0인 지점에 말을 놓을 수 있다



# 현재 좌표에 퀸을 놓을 수 있는지 여부 체크
def check(x, y):

    dx = [-1, -1, -1]
    dy = [-1, 0, 1]   # 각각 좌상단, 위쪽, 우상단을 체크함

    for i in range(3):
        for k in range(1, N):   # 현재 check 지점에서 0행/0열/N행/N열까지 체크
            new_x = x + dx[i]*k
            new_y = y + dy[i]*k
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                break
            if pan[new_x][new_y] == 1:
                return 0   # 이미 퀸이 놓아져 있어 불가

    return 1   # 퀸을 놓을 수 있다


# 현재 행에서 모든 열에 퀸을 놓는 경우
def DFS(depth):

    global sol, N

    if depth >= N:  # N행이 되면 멈춘다
        sol += 1
        return

    # 기본 check 함수 사용한 for문
    # for i in range(N):  # i는 열에 해당한다
    #     if check(depth, i):   # 현재 행과 열을 check함수로 넘긴다
    #         pan[depth][i] = 1  # 퀸 놓기
    #         DFS(depth+1)   # 다음 행으로 넘어가기
    #         pan[depth][i] = 0  # 아니면 퀸을 빼기

    for i in range(N):
        if chk1[i]:  # 세로 방향 체크
            continue
        if chk2[depth+i]:  # 오른쪽 대각선 방향 체크
            continue
        if chk3[(N-1)-(depth-i)]:  # 왼쪽 대각선 방향 체크
            continue

        chk1[i] = chk2[depth+i] = chk3[(N-1)-(depth-i)] = 1
        DFS(depth+1)
        chk1[i] = chk2[depth+i] = chk3[(N-1)-(depth-i)] = 0


# 백트래킹 - 모든 경우의 수를 구해야 하므로 가지치기가 필요하다
N = int(input())

pan = [[0 for _ in range(N)] for _ in range(N)]

sol = 0

# 개선된 백트래킹 - depth를 찾고 어떤 것을 반복시킬지 고민할 것
chk1 = [0] * N
chk2 = [0] * (2*N)
chk3 = [0] * (2*N)

DFS(0)   # 0행부터 시작

print(sol)
