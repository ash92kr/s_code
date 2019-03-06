import sys
sys.stdin = open("노드의 합_input.txt")

def make_sum(tree):

    global N, M

    # 트리를 조사하니 전체 길이의 N//2+1부터 값이 들어가 있었다
    for i in range(N, 0, -1):   # 따라서 역순으로 살펴보면서
        if tree[i] == 0:    # i번 인덱스에 0번 값이 들어갔으면
            if i*2 <= N:   # 왼쪽 자식 노드가 있으면
                tree[i] += tree[i*2]   # 부모 노드에 더하고
                if i*2+1 <= N:   # 오른쪽 자식 노드가 있으면
                    tree[i] += tree[i*2+1]   # 역시 부모 노드에 더한다

    return tree


T = int(input())

for tc in range(T):
    
    # N = 전체 노드 개수, M = 리프 노드 개수, L = 값을 알고 싶은 노드 번호
    N, M, L = map(int, input().split())
    
    leaf = []   # 리프 노드에 해당하는 값 받기

    for i in range(M):
        leaf += list(map(int, input().split()))

    tree = [0] * (N+1)   # 전체 트리 만들기

    for i in range(len(leaf)//2):   # 우선 리프 노드부터 받자
        tree[leaf[i*2]] = leaf[i*2+1]

    make_sum(tree)
    # print(tree)

    print("#{} {}".format(tc+1, tree[L]))   # L번 노드의 값 출력하기
