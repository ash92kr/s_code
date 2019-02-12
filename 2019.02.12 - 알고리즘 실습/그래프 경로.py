import sys
sys.stdin = open("그래프 경로_input.txt")

def reach(S):

    global V, E, line, matrix, G, visited   # 전역변수화

    visited[S] = 1   # 출발 노드 및 인접 노드는 무조건 방문했다고 표시

    for i in range(V+1):   # 인접행렬의 행 개수만큼 반복
        if matrix[S][i] == 1 and visited[i] == 0:   # 인접행렬의 출발 노드와 연결된 노드 + 아직 방문하지 않은 경우
            reach(i)   # i번 노드로 이동해서 위를 반복함 ex) 1 -> 4이면 4로 이동하고 4 -> 6으로 순환 

    if visited[G] == 1:   # 도착 노드에 방문했다고 표시되면 1 반환
        return 1
    else:
        return 0   # 도착 노드에 방문하지 못했다고 표시되면 0 반환

T = int(input())

for tc in range(T):

    V, E = map(int, input().split())   # V = 노드 개수, E = 간선 개수
    line = []   # 노드 연결 정보(어떤 노드가 연결되었는지 보여주는 정보)

    for i in range(E):
        line += list(map(int, input().split()))

    S, G = map(int, input().split())   # S = 출발 노드, G = 도착 노드

    matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]   # 인접행렬 생성
    visited = [0] * (V+1)  # 방문한 노드 표시하는 스택

    for j in range(0, len(line), 2):   # 인접행렬에 노드 연결정보 채우기
        matrix[line[j]][line[j+1]] = 1   # 방향성 있는 정보 채우기(x=진입, y=진출)

    # for k in range(len(matrix)):
    #     print(f'{k} {matrix[k]}')

    print(f'#{tc+1} {reach(S)}')

