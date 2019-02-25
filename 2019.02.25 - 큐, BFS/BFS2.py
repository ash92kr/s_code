def BFS(G, v):

    global N, K, visited

    queue = []
    queue.append(v)

    visited[v] = 1   # enqueue할 때 visited 체크
    print(v, end=" ")

    while queue:  # len(queue) >= 1
        t = queue.pop(0)

        for i in range(1, N+1):
            if G[t][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1
                print(i, end=" ")


N, K = 7, 8
line = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

G = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(0, len(line), 2):
    G[line[i]][line[i+1]] = 1
    G[line[i+1]][line[i]] = 1

visited = [0] * (N+1)

BFS(G, 1)
print(max(visited))