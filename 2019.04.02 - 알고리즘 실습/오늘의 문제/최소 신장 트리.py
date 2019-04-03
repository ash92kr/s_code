import sys
sys.stdin = open("최소 신장 트리_input.txt")

def findset(x):

    if x == p[x]:
        return x
    else:
        return findset(p[x])   # 부모 넣기

def mst():

    global V

    c = 0  # 간선개수
    s = 0  # 가중치의 합
    i = 0  # 제어변수

    while c < V:  # count는 V 이하로만 돌아야 한다

        p1 = findset(edge[i][0])   # 대표자를 가져온다
        p2 = findset(edge[i][1])   # edge의 시작 정점과 도착 정점을 가져온다
        if p1 != p2:  # 사이클이 생성되지 않으면
            s += edge[i][2]   # s에 weight을 더함
            c += 1
            p[p2] = p1   # union 대용(p2의 부모는 p1)
        i += 1

    return s


T = int(input())

for tc in range(T):

    V, E = map(int, input().split())

    edge = [list(map(int, input().split())) for _ in range(E)]   # 간선의 개수는 V와 상관없다

    # for i in range(0, len(edge)-1):
    #     for j in range(i+1, len(edge)):
    #         if edge[i][2] > edge[j][2]:
    #             edge[i], edge[j] = edge[j], edge[i]
    #         elif edge[i][2] == edge[j][2]:
    #             if edge[i][1] > edge[j][1]:
    #                 edge[i], edge[j] = edge[j], edge[i]
    #             elif edge[i][1] == edge[j][1]:
    #                 if edge[i][0] > edge[i][0]:
    #                     edge[i], edge[j] = edge[j], edge[i]

    edge.sort(key=lambda x: x[2])  # 3열을 기준으로 정렬함

    # print(weight)

    # data = []
    #
    # for i in range(V+1):
    #     data.append(i)
    #
    # print(data)

    adj = [[0] * (V+1) for _ in range(V+1)]  # ??

    p = list(range(V+1))   # 대표 원소 초기화 - 부모 원소 넣기

    # mst()

    print("#{} {}".format(tc+1, mst()))


    # print(weight)

    # KRUSKAL(weight, 0)




