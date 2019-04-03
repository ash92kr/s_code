import sys
sys.stdin = open("최소 이동 거리_input.txt")


def getMinIdx():
    minV = 9999999
    minIdx = 0

    for i in range(N+1):
        if visit[i] == 0 and D[i] < minV:   # 방문 안 한 노드 중 D가 최소인 노드 찾기
            minIdx = i
            minV = D[i]

    return minIdx


def dijkstra(goal):

    D[0] = 0   # 출발점의 가중치(출발점을 지정해야 한다)

    for i in range(N+1):
        if adj[0][i]:   # 출발점과 인접한 노드
            D[i] = adj[0][i]   # D 초기화

    visit[0] = 1   # 시작 노드 방문

    while True:
        node = getMinIdx()   # 노드 중 가장 작은 것 찾기
        visit[node] = 1   # D가 가장 작은 노드 방문처리
        if node == goal:   # 도착지에 도착하면
            return D[goal]   # 그 곳의 가중치 반환

        for x in range(N+1):
            if adj[node][x]:   # minIdx에 인접한 노드에 대해
                if D[x] > (D[node] + adj[node][x]):   # minIdx를 경유하는 비용이 직선 거리보다 작으면
                    D[x] = D[node] + adj[node][x]   # D[x] 갱신


T = int(input())

for tc in range(T):

    N, E = map(int, input().split())  # 0부터 N까지 이동

    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]

    visit = [0] * (N+1)

    D = [9999999] * (N+1)

    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w   # 방향성 있음

    print("#{} {}".format(tc+1, dijkstra(N)))




