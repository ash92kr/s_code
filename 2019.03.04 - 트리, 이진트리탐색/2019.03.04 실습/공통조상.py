import sys
sys.stdin = open("공통조상_input.txt")


def ancestor(N1, N2):

    global tree, V, E

    # N1_anc = [0] * (V+1)
    # N2_anc = [0] * (V+1)

    anc = []
    anc_node = 0

    while True:
        if tree[N1][2] == 0:
            break
        else:
            anc.append(tree[N1][2])

        N1 = tree[N1][2]

    while True:
        if tree[N2][2] == 0:
            break
        else:
            anc.append(tree[N2][2])

        N2 = tree[N2][2]

    # print(anc)

    for i in range(0, len(anc)-1):
        flag = 0
        for j in range(i+1, len(anc)):
            if anc[i] == anc[j]:
                anc_node = anc[i]
                flag = 1
                break
        if flag == 1:
            break

    root_count(anc_node)

    return anc_node


def root_count(node):

    count = 0

    if node != 0:
        root_count(tree[node][0])
        count += 1
        root_count(tree[node][1])

    return count


T = int(input())

for tc in range(T):
    # V = 총 노드 개수, E = 총 간선 개수, N1/N2 = 공통조상을 찾기 위한 2개의 노드
    V, E, N1, N2 = map(int, input().split())

    data = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(V+1)]

    for i in range(len(data)//2):
        n1 = data[i*2]
        n2 = data[i*2 + 1]
        if tree[n1][0] == 0:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1

    # print(tree)

    print("#{}".format(tc+1), end=" ")
    print(ancestor(N1, N2))
    # print(root_count())