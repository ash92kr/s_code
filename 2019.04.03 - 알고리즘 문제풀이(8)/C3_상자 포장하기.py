import sys
sys.stdin = open("C3_상자 포장하기_input.txt")

def DFS(depth, a_last, b_last, hab):

    global max_hab

    if depth >= N:
        # if max_hab < (a_sum + b_sum):
        #     max_hab = (a_sum + b_sum)
        if max_hab < hab:
            max_hab = hab
        return

    # if a_last > box[depth] and check[depth] == 0:
    if a_last > box[depth]:
        a_last = box[depth]
    # check[depth] = 1
    DFS(depth+1, a_last, b_last, hab+box[depth])

    # if box[depth] > b_last and check[depth] == 0:
    if box[depth] > b_last:
        b_last = box[depth]
    # check[depth] = 1
    DFS(depth+1, a_last, b_last, hab+box[depth])

    # check[depth] = 0
    DFS(depth+1, a_last, b_last, hab)



# 사용되지 않는 상자가 있으므로 조합으로 풀어야 한다

T = int(input())

for tc in range(T):

    N = int(input())

    box = list(map(int, input().split()))

    record = [0] * N
    # check = [0] * N

    max_hab = 0

    # a_last = 1001   # 마지막으로 포장한 상자를 들고 다녀야 한다
    # b_last = 0    # 초기값을 주는 것도 고려(a는 min 비교, b는 max 비교)

    DFS(0, 1001, 0, 0)   # 필요한 파라미터 - 상자 인덱스 번호, A/B의 최근에 넣은 상자, A/B의 합

    print(max_hab)
