import sys
sys.stdin = open("작업순서_input.txt")

def path(S):

    global V, E, graph, visited, hap

    weight = [0] * (V+1)   # hap과 비교하기 위한 리스트
    order = []   # 작업 순서대로 출력할 리스트

    for i in range(len(S)):
        visited[S[i]] = 1
        order.append(i)
        weight[i] += 1

        for j in range(V+1):
            if graph[i][j] == 1 and visited[i] == 0:
                if weight[i] < hap[i]:
                    weight[i] += 1
                else:
                    path(i)

    return order


for tc in range(1):

    V, E = map(int, input().split())   # V = 정점의 개수, E = 간선의 개수

    chain = list(map(int, input().split()))

    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]

    visited = [0] * len(graph)
    hap = [0] * (V+1)    # 진입차수를 구하는 리스트
    S = []    # 스타팅 포인트

    for i in range(0, len(chain), 2):
        graph[chain[i]][chain[i+1]] = 1

    for i in range(1, len(chain), 2):
        hap[chain[i]] += 1

    for i in range(len(hap)):
        if hap[i] == 0 and i != 0:
            S.append(i)

    print(f'#{tc+1} {path(S)}')








