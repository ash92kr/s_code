import sys
sys.stdin = open("중위순회_input.txt")

def inorder(node):
    if node:   # node가 있으면
        inorder(firstChild[node])   # 우선 왼쪽 자식노드부터 있는지 확인
        print(alpha[node], end="")   # 없으면 해당 문자를 출력
        inorder(secondChild[node])   # 왼쪽과 가운데를 모두 탐색하면 오른쪽 자식노드 확인

T = 10
for tc in range(T):
    N = int(input())
    firstChild = [0] * (N+1)   # 왼쪽 자식노드 저장하기 위한 배열
    secondChild = [0] * (N+1)   # 오른쪽 자식노드 저장하기 위한 배열
    alpha = [0] * (N+1)   # 문자열 저장하기 위한 배열

    for i in range(N):
        temp = list(input().split())   # 노드 번호, 문자, 숫자 받기 위한 리스트
        addr = int(temp[0])   # 노드 번호
        ch = temp[1]   # 문자
        alpha[addr] = ch   # alpha 배열의 addr 인덱스에 문자열을 넣음
        if addr * 2 <= N:   # addr * 2가 N보다 작을 때만 왼쪽 노드를 만들 수 있다
            firstChild[addr] = int(temp[2])   # 첫 번째 숫자를 왼쪽 배열에 넣음
            if addr * 2 + 1 <= N:   # addr * 2 + 1이 N보다 작을 때만 오른쪽 노드를 만들 수 있다
                secondChild[addr] = int(temp[3])   # 두 번째 숫자를 오른쪽 배열에 넣음

    # print(firstChild)
    # print(secondChild)
    # print(alpha)

    print("#{}".format(tc+1), end=" ")   # 함수의 return값이 없어 이렇게 따로 print를 써야 함
    inorder(1)
    print()