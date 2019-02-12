# import sys
# sys.stdin = open("")

def DFS_Recursive(matrix, start):  # 인접행렬, 시작점

    visited[start] = 1
    print(f'{start}', end=" ")

    for i in range(1, len(matrix[start-1])):   # v에 인접한 모든 정점들
        if visited[i] == 0 and matrix[start][i] == 1:  # 방문 안 하고 인접 정점이어야 한다
            DFS_Recursive(matrix, i)

    # 재귀함수의 return - flag를 사용해 원하는 곳까지 도달하면 끝낼 것


# n, e = map(int, input().split())    # 정점과 간선의 개수
# n += 1    # 정점의 개수 + 1로 만들어야 한다
# temp = list(map(int, input().split()))

n, e = 8, 8
temp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

G = [[0 for i in range(n)] for j in range(n)]  # 2차원 배열 초기화(인접행렬)
visited = [0 for i in range(n)]   # 방문한 정점 스택

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1   # 이것만 적으면 방향성이 있는 행렬
    G[temp[i+1]][temp[i]] = 1   # 2차원 행렬이므로 둘 다 적어야 한다

for i in range(n):
    print(f'{i} {G[i]}')   # 입력확인

DFS_Recursive(G, 1)   # 인접행렬(참조타입이므로 안 넘겨줘도 됨), 시작점



def dfs(v):
    global G, visited, n   # 매개변수를 넘기지 않으면 n은 넘기지 않음
    visited[v] = 1
    print(v, end=" ")

    for w in range(n):
        if G[v][w] == 1 and visited[w] == 0:   # 가중치가 있으면 G[v][w] == 1 조건 제외
            dfs(w)    # 인접한 정점 중 방문하지 않은 정점을 재귀함수에 넣음

dfs(1)






