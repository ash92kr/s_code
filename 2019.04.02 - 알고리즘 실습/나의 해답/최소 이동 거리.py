import sys
sys.stdin = open("최소 이동 거리_input.txt")

def min_idx():

    min_value = 987654321
    min_idx = 0

    for i in range(N+1):
        if visited[i] == 0 and D[i] < min_value:
            min_idx = i   # 이것만 중요하다
            min_value = D[i]

    return min_idx


def dijkstra(goal):
    
    D[0] = 0  # 출발점 가중치 초기화

    for i in range(N+1):
        if adj[0][i]:   # 출발점과 연결된 경우
            D[i] = adj[0][i]   # 가중치 변경

    visited[0] = 1  # 시작 노드 방문

    while True:

        node = min_idx()   # 시작 노드에서 가장 가중치가 작은 노드 선택
        visited[node] = 1   # 해당 노드 방문

        if node == goal:   # 그 노드가 목적지라면 목적지의 누계 가중치 return
            return D[goal]

        for j in range(N+1):  # 현재 노드에서 인접한 정점 찾기
            if adj[node][j]:  # 인접했다면(1로 표시됨)
                if D[j] > D[node] + adj[node][j]:   # 현재 노드 + 인접 가중치가 기존값보다 작은 경우
                    D[j] = D[node] + adj[node][j]


T = int(input())

for tc in range(T):
    
    N, E = map(int, input().split())
    
    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]   # 인접 행렬
    
    visited = [0] * (N+1)  # 방문 배열
    
    D = [987654321] * (N+1)   # 가중치 배열
    
    for i in range(E):
        s, e, d = map(int, input().split())
        adj[s][e] = d

    print("#{} {}".format(tc+1, dijkstra(N)))

