import sys
sys.stdin = open("사람 네트워크2_input.txt")

T = int(input())

for tc in range(T):

    temp = list(map(int, input().split()))

    N = temp.pop(0)

    adj = [[0] * N for _ in range(N)]    # 대각선은 0을 넣어야 한다

    idx = 0

    for i in range(0, N):
        for j in range(0, N):
            adj[i][j] = temp[idx]
            if i != j and adj[i][j] == 0:  # 대각선이 아니되 0인 곳은 초기값으로 무한대를 넣음
                adj[i][j] = 987654321
            idx += 1

    # 프로이드 알고리즘
    for k in range(N):
        for i in range(N):
            if i == k:   # 자기 자신은 제외
                continue
            for j in range(i+1, N, 1):   # 대각선의 어느 한 방향만 고려하면 된다
                if j == k or j == i:   # 마찬가지로 자기 자신은 제외
                    continue
                if adj[i][j] > adj[i][k] + adj[k][j]:   # 경유지의 값이 직선거리보다 낮으면 낮은 값으로 변경한다
                    adj[j][i] = adj[i][j] = adj[i][k] + adj[k][j]

    minV = 987654321
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += adj[i][j]

        if sum < minV:   # i부터 j까지 가는 최단 경로의 수를 더한다
            minV = sum

    print("#{} {}".format(tc+1, minV))
