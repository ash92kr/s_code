import sys
sys.stdin = open("이진탐색_input.txt")

def inorder(node):

    global tree, N, idx

    if node <= N:   # node번호가 N보다 작을 때만 실시
        inorder(node*2)   # 왼쪽 자식 노드
        tree[node] = idx   # 이진탐색트리의 노드(인덱스)에 값을 넣는다
        idx += 1   # 값에 1을 추가한다
        inorder(node*2+1)   # 오른쪽 자식 노드


T = int(input())

for tc in range(T):

    N = int(input())   # 노드 개수

    tree = [0] * (N+1)   # 이진탐색트리(노드 개수 + 1)
    root = 1   # 시작할 루트 번호
    idx = 1   # 값을 넣기 위한 변수

    inorder(root)

    print("#{} {} {}".format(tc+1, tree[1], tree[N//2]))


