import sys
sys.stdin = open("반사경_input.txt", "r")
T = int(input())

def solve():
    global ans, dir
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 0, 0
    while True:
        visit[x][y] = 1
        x += dx[dir]
        y += dy[dir]

        if x < 0 or x >= N or y < 0 or y >= N: return
        if arr[x][y] == 2:  # \
            if dir == 0 :   dir = 1
            elif dir == 1 : dir = 0
            elif dir == 2 : dir = 3
            elif dir == 3 : dir = 2
            ans += 1
        elif arr[x][y] == 1: # /
            if dir == 0:    dir = 3
            elif dir == 1:  dir = 2
            elif dir == 2:  dir  = 1
            elif dir == 3:  dir = 0
            ans += 1

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    ans = 0
    dir = 0

    solve()
    print("#{} {}".format(tc+1, ans))
    for i in range(N):
        print(visit[i])
    print()