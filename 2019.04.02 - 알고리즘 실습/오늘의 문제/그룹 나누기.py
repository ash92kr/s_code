import sys
sys.stdin = open("그룹 나누기_input.txt")

def union(x, y):   # y의 부모로 x를 지정

    p[find_set(y)] = p[find_set(x)]   # 최상단 부모의 값을 자식에 넣음


def find_set(x):

    if x == p[x]:  # 어떤 정점의 부모가 자기 자신이면 종료
        return x
    else:   # 어떤 정점의 부모가 자기 자신이 아니면 계속해서 부모로 이동
        return find_set(p[x])


T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    card = list(map(int, input().split()))

    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]   # 인접 행렬

    for i in range(0, len(card), 2):
        adj[card[i]][card[i+1]] = 1
        adj[card[i+1]][card[i]] = 1

    # for i in range(N+1):
    #     print(i, adj[i])

    p = [ _ for _ in range(N+1)]   # 같은 조를 표시하기 위한 행렬(make_set)

    # print(p)

    for i in range(len(adj)):
        for j in range(i+1, len(adj)):   # 대각선 기준 위쪽만 실시
            if adj[i][j] == 1:
                union(i, j)   # union(j(열)의 부모를 i(행)로 지정) - 여기가 핵심

    # print(p)

    count = 0

    for k in range(1, len(p)):   # 정점이 자기 자신을 호출하는 경우 하나의 조에 해당
        if k == p[k]:
            count += 1

    print("#{} {}".format(tc+1, count))