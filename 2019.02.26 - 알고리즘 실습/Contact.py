import sys
sys.stdin = open("Contact_input.txt")


def emergency(v):

    global telephone, matrix, visited

    queue = []
    queue.append(v)

    visited[v] = 1

    while queue:
        t = queue.pop(0)

        for i in range(int(matrix//2)):




    m_visited = 0

    for j in range(len(visited)):
        if visited[j] != 0:
            m_visited = j

    return m_visited


for tc in range(10):

    L, S = map(int, input().split())  # L = 전체 길이, S = 시작점
    telephone = list(map(int, input().split()))

    matrix = [[0 for _ in range(max(telephone)+1)] for _ in range(max(telephone)+1)]

    for i in range(0, len(telephone), 2):
        matrix[telephone[i]][telephone[i+1]] = 1

    visited = [0] * (max(telephone)+1)

    print(f'#{tc+1} {emergency(S)}')




