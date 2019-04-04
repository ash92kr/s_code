# 방향성이 있는가? 가중치를 구해야 하는가?

# 출제방식1 - 연결정보를 알려준다
# start - end - start의 연결법을 알려주어야 한다
# 무방향성은 양쪽에 1을 표시해야 한다
# 인접행렬의 크기(N+1)만큼 만들기

# 행이 현재 나의 위치, 열은 나와 연결된 인접정점
# 따라서 행을 기준으로 인접행렬을 보아야 한다

# 중복 방문할 필요가 없어서 visit 체크 필요
# 그래프는 연결된 간선만 따라가므로 depth가 끝까지 갈 필요가 없다
# 나와 연결된 간선을 따라갈 때 depth+1이 된다
# 현재 위치에서 더 이상 시도할 것이 없으면 함수가 끝난다
# 함수가 닫힐 때(더 이상 연결된 정점이 없을 때) 값을 반환함

import sys
sys.stdin = open("D0_바이러스_input.txt")


def BFS(x):

    queue = []
    queue.append(x)

    visit[x] = 1

    while queue:

        x = queue.pop(0)

        for i in range(N+1):
            if arr[x][i] == 1 and visit[i] == 0:
                queue.append(i)
                visit[i] = 1


def DFS(x):

    global cnt

    for i in range(N+1):
        if arr[x][i] == 1 and visit2[i] == 0:
            visit2[i] = 1   # 다음에 갈 컴퓨터 체크
            cnt += 1
            DFS(i)

    return cnt


N = int(input())
M = int(input())

arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1

visit = [0] * (N+1)

BFS(1)

count = 0

for i in range(2, N+1):
    if visit[i] != 0:
        count += 1

print(count)

visit2 = [0] * (N+1)
visit2[1] = 1   # 이 부분은 카운트에서 제외(하지만 시작 전에 체크해야 한다)

cnt = 0

print(DFS(1))


