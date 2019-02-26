import sys
sys.stdin = open("노드의 거리_input.txt")


def node_count(v):

    global matrix, visited, G

    queue = []
    queue.append(v)

    visited[v] = 1   # 출발점에 1을 줌

    while queue:

        t = queue.pop(0)

        for i in range(1, len(matrix)):
            if matrix[t][i] == 1 and visited[i] == 0:   # 인접행렬이 1로 표시되고 아직 방문하지 않은 경우
                queue.append(i)   # 인접한 정점들을 큐에 추가한다
                visited[i] = visited[t] + 1   # 또한, 인접한 정점을 방문했다고 표시

           if t == G:   # 시작 좌표가 Goal에 도달하면
            return visited[t] - 1   # 해당 visited의 좌표에서 1을 뺀 값을 출력한다
    return 0   # 틀릴 경우에 한정

T = int(input())

for tc in range(T):

    V, E = map(int, input().split())   # V = 노드 개수, E = 간선 개수

    line = []   # 간선들을 모아놓은 행렬

    for i in range(E):
        line.append(list(map(int, input().split())))

    matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for i in range(len(line)):   # 무방향성 간선 인접행렬에 표시(둘 다 표시해야 함)
        matrix[line[i][0]][line[i][1]] = 1
        matrix[line[i][1]][line[i][0]] = 1

    S, G = map(int, input().split())   # S = 출발 노드, G = 도착 노드

    visited = [0] * (V+1)

    print(f'#{tc+1} {node_count(S)}')
