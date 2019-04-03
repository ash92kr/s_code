import sys
sys.stdin = open("C2_양팔저울_input.txt")


def DFS(depth, l_hap, r_hap):

    global flag

    if flag == 'Y':   # 가지치기
        return
    
    # 남은 추의 무게를 가지고 양팔 저울의 무게 비교

    if depth >= N:
        # for i in range(N):
        #     print(left[i], end=" ")
        #     print(right[i], end=" ")
            # print(rec[i], end=" ")
        # print()
        # if count == 1:
        if l_hap == r_hap:  # 양쪽저울무게가 같으면 성공
            flag = 'Y'
        return

    # left[depth] = weight[depth]
    # DFS(depth+1, l_hap+weight[depth], r_hap)
    #
    # right[depth] = weight[depth]
    # DFS(depth+1, l_hap, r_hap+weight[depth])
    #
    # left[depth] = 0
    # right[depth] = 0
    # DFS(depth+1, l_hap, r_hap)

    # 현재 추를 사용하거나 사용하지 않기(왼쪽, 오른쪽 저울에 사용)
    rec[depth] = weight[depth]
    DFS(depth+1, l_hap+weight[depth], r_hap)  # 현재추를 왼쪽에 올리기
    DFS(depth+1, l_hap, r_hap+weight[depth])  # 현재추를 오른쪽에 올리기

    rec[depth] = 0
    DFS(depth+1, l_hap, r_hap)   # 현재추를 사용하지 않기


# 어떤 시도를 해야 하면 조합이어도 삼중재귀, 사중재귀가 될 수도 있다
# 어느 쪽에 올리는가에 따라 경우의 수가 많아진다

#       X  왼쪽  오른쪽
#  1g
#  4g

# 즉, 왼쪽의 합계와 오른쪽의 합계 2개를 들고 다녀야 한다
# 왼쪽 저울의 합계와 오른쪽 저울의 합계가 같으면 종료
# 초기값인 구슬의 무게도 왼쪽에 넣고 시작한다

# 왼쪽 저울의 무게 - 3+1+4, 3+1, 3
# 오른쪽 저울의 무게 -  0, 4, 1+4
# 양쪽에 한 개씩 올린 경우

N = int(input())

weight = list(map(int, input().split()))

M = int(input())

marble = list(map(int, input().split()))

# left = [0] * N
# right = [0] * N

rec = [0] * N  # 기록배열

for i in range(M):
    # left = marble[i]
    # right = 0
    # print(DFS(0, 0, 0), end=" ")
    flag = 'N'
    DFS(0, marble[i], 0)
    print(flag, end=" ")
