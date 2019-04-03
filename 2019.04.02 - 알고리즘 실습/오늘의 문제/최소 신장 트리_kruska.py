import sys
sys.stdin = open("최소 신장 트리_input.txt")

def find_set(x):

    if x != p[x]:
        return find_set(p[x])
    else:
        return x


def kruskal(data, start):

    global V

    c = 0   # 간선 개수 더하는 변수
    w = 0   # 간선 가중치 더하는 변수
    i = 0

    while c < V:   # c(선택한 간선 개수)가 V-1일 때까지 실행

        p1 = find_set(data[i][0])
        p2 = find_set(data[i][1])

        if p1 != p2:  # 부모가 다른 경우(사이클이 생성되지 않음)
            w += data[i][2]
            c += 1
            p[p2] = p1  # 부모를 넣음

        i += 1

    return w


T = int(input())

for tc in range(T):

    V, E = map(int, input().split())

    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]

    data = [list(map(int, input().split())) for _ in range(E)]

    # for i in range(E):
    #     data.append(list(map(int, input().split())))
    #     adj[data[i][0]][data[i][1]] = data[2]
    #     adj[data[1]][data[0]] = data[2]

    # for i in range(len(adj)):
    #     print(i, adj[i])

    # 버블 정렬은 제한시간 초과로 불가능
    # for i in range(0, E-1):
    #     for j in range(i+1, E):
    #         if data[i][2] > data[j][2]:
    #             data[i], data[j] = data[j], data[i]

    data.sort(key=lambda x : x[2])
    # print(data)

    p = [ _ for _ in range(V+1)]

    # print(p)

    print("#{} {}".format(tc+1, kruskal(data, 0)))



