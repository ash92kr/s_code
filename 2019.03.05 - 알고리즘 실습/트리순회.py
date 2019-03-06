import sys
sys.stdin = open("트리순회_input.txt")


def printTree():
    for i in range(1, V+1):
        print("%2d %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2]))   # C 스타일 출력법
# %.0f  -> 소수점 아래 자릿수가 하나도 없다

# 아래의 함수들은 처음 노드에서 시작했다가 다시 처음 노드로 돌아와야 끝난다
def preorder(node):
    if node != 0:   # 해당 노드의 자식 노드가 없다면 아무 것도 반환하지 않음 -> 만약 있으면 아래를 실시함
        print("{}".format(node), end=" ")   # 무조건 실시함(현재 노드(부모 노드)의 번호 출력)
        preorder(tree[node][0])   # 좌측 노드부터 탐색(재귀함수이므로 None을 반환)
        preorder(tree[node][1])

def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print("{}".format(node), end=" ")
        inorder(tree[node][1])

def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print("{}".format(node), end=" ")


V, E = map(int, input().split())
tree = [[0 for _ in range(3)] for _ in range(V+1)]   # left, right, parent 배열 만들기(0번 행 사용X)
temp = list(map(int, input().split()))

for i in range(E):
    n1 = temp[i * 2]
    n2 = temp[i * 2 + 1]
    if not tree[n1][0]:   # tree[n1]행의 1열이 0이면(비었으면)
        tree[n1][0] = n2   # 왼쪽 자식 노드에 해당
    else:
        tree[n1][1] = n2   # 값이 있으면 오른쪽 자식 노드에 해당
    tree[n2][2] = n1   # 해당 행의 3열에는 부모 노드를 넣음(간선으로 연결되었으므로)

print(tree)
printTree()

preorder(1)
print()

inorder(1)
print()

postorder(1)
print()



