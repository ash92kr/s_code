import sys
sys.stdin = open("C4_주사위 던지기1_input.txt")

def DFS_1(depth):   # 중복순열

    if depth >= N:
        for i in range(N):
            print(record[i], end=" ")
        print()
        return

    for i in range(6):   # 눈(처음부터 끝까지 모두 출력)
        record[depth] = i+1
        DFS_1(depth+1)

# 중복조합
def DFS_2(depth, start):   # depth = 주사위, start = 시작 눈

    if depth >= N:
        for i in range(N):
            print(record[i], end=" ")
        print()
        return

    for i in range(start, 6):  # start부터 시작하므로 그 이전은 고려하지 않음
        record[depth] = i+1
        # DFS_2(depth+1, start+1)
        DFS_2(depth+1, i)   # 하나의 배열에 중복 숫자 제거하기

# 순열 - 중복 제거
def DFS_3(depth):

    if depth >= N:
        for i in range(N):
            print(record[i], end=" ")
        print()
        return

    for i in range(6):
        if check[i]:
            continue
        record[depth] = i+1   # 눈 기록
        check[i] = 1
        DFS_3(depth+1)
        check[i] = 0

# 조합
def DFS_4(depth, start):

    if depth >= N:   # 다중재귀일 경우 N는 depth이다(몇 개까지 뽑을 것인가?)
        for i in range(N):
            print(record[i], end=" ")
        print()
        return

    for i in range(start, 6):
        record[depth] = i+1
        DFS_4(depth+1, i+1)


N, M = map(int, input().split())

# nun = [1, 2, 3, 4, 5, 6]
record = [0] * (N+1)
check = [0] * 7  # 체크 배열이므로 dfs3에서는 7이 되어야 한다

if M == 1:
    DFS_1(0)
elif M == 2:
    DFS_2(0, 0)
elif M == 3:
    DFS_3(0)
elif M == 4:
    DFS_4(0, 0)