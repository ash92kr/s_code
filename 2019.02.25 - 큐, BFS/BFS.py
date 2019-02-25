def BFS(G, v):

    global N, E

    visited = [0] * (N+1)
    queue = []
    queue.append(v)  # 시작 정점 넣기
    while queue:  # len(queue) >= 1
        t = queue.pop(0)   # 큐는 가장 앞에서 값을 뺀다
        if not visited[t]:   # visited[t] == False
            visited[t] = True
            print(t, end=" ")

            for i in range(1, len(G[t])):
                if G[t][i] == 1 and not visited[i]:   # 인접행렬의 경우 1인 칸과 방문하지 않은 곳을 찾아야 한다
                    queue.append(i)


N, E = 7, 8
line = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

G = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(0, len(line), 2):
    G[line[i]][line[i+1]] = 1
    G[line[i+1]][line[i]] = 1

for i in range(N+1):   # 8번까지 만들어야 한다
    print(f'{i} {G[i]}')

BFS(G, 1)