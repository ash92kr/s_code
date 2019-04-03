import sys
sys.stdin = open("최소 신장 트리_input.txt")

def mst():

    global V

    total = 0
    u = 0   # 시작점을 0으로
    D[u] = 0
    PI[u] = 0   # 가중치와 부모를 바꿈

    for i in range(V+1):
        min = 0x7fffffff
        for v in range(V+1):
            if visit[v] == 0 and min > D[v]:
                min = D[v]
                u = v

        visit[u] = 1
        total += adj[PI[u]][u]

        for v in range(V+1):   # 인접한 정점 업데이트
            if adj[u][v] != 0 and visit[v] == 0 and adj[u][v] < D[v]:
                D[v] = adj[u][v]
                PI[v] = u

    return total


T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())

    adj = [[0]*(V+1) for _ in range(V+1)]   # 인접행렬 채우기

    D = [987654321] * (V+1)   # 가중치

    PI = list(range(V+1))  # 부모값

    visit = [0] * (V+1)   # 방문 행렬

    for i in range(E):
        edge = list(map(int, input().split()))

        for j in range(len(edge)):
            adj[edge[0]][edge[1]] = edge[2]
            adj[edge[1]][edge[0]] = edge[2]
    
    print("#{} {}".format(tc, mst()))
 
