import sys
sys.stdin = open("Contact_input.txt")


def emergency(v):

    global telephone, matrix, visited

    queue = []   # 큐에 시작점을 넣음
    queue.append(v)

    visited[v] = 1   # 시작점을 방문했다고 표시

    while queue:
        t = queue.pop(0)   # 큐의 처음을 뽑아냄

        for i in range(1, len(matrix)):
            if matrix[t][i] == 1 and visited[i] == 0:   # 큐의 처음 정점과 연결되었으며, 방문하지 않았다면
                queue.append(i)   # 큐의 마지막에 넣고
                visited[i] = visited[t] + 1   # visited의 값으로 +1을 추가함

    last = 0   # 인덱스 뽑기

    for j in range(len(visited)):
        if visited[j] == max(visited):   # visited를 순회하면서 max값과 같은 경우의 인덱스를 넣음
            last = j   # max값이 여러 개라면 가장 마지막의 인덱스를 넣고 return함

    return last


    # m_visited = 0
    #
    # for j in range(len(visited)):
    #     if visited[j] != 0:
    #         m_visited = j
    #
    # return m_visited


for tc in range(10):

    L, S = map(int, input().split())  # L = 전체 길이, S = 시작점
    telephone = list(map(int, input().split()))   # 데이터 받기

    matrix = [[0 for _ in range(max(telephone)+1)] for _ in range(max(telephone)+1)]

    for i in range(0, len(telephone), 2):   # 인접 행렬
        matrix[telephone[i]][telephone[i+1]] = 1

    visited = [0] * (max(telephone)+1)   # 방문 행렬

    # for i in range(len(matrix)):
    #     print(i, matrix[i])

    print(f'#{tc+1} {emergency(S)}')

