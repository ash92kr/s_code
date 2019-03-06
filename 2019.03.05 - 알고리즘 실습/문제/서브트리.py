import sys
sys.stdin = open("서브트리_input.txt")

def count_node(node):   # 순회 방법은 아무거나 상관 없음

    global cnt

    if node != 0:
        count_node(tree[node][0])
        cnt += 1
        count_node(tree[node][1])

    return cnt


T = int(input())

for tc in range(T):

    E, N = map(int, input().split())  # E = 간선 개수, N = 시작 노드

    tree = [[0 for _ in range(3)] for _ in range(E+2)]   # 3열 E+2행(간선 개수 + 1 = 노드 개수)
    data = list(map(int, input().split()))
    cnt = 0

    for i in range(len(data)//2):
        n1 = data[i*2]   # 부모 노드
        n2 = data[i*2+1]   # 자식 노드
        if tree[n1][0] == 0:  # 0열의 값이 없으면 왼쪽 자식 노드에 값 입력
            tree[n1][0] = n2
        else:    # 0열의 값이 있으면 오른쪽 자식 노드에 값 입력
            tree[n1][1] = n2
        tree[n2][2] = n1   # 자식 노드의 2열에 부모 노드 값 입력

    cnt = count_node(N)   # 해당 노드부터 시작하는 부분 트리의 원소 구하기

    print("#{} {}".format(tc+1, cnt))

