import sys
sys.stdin = open("C4_주사위 던지기1_input.txt")

# 순열과 조합의 또 다른 경우
# M에 따라 다르게 출력할 것

# M=1일 때는 중복순열(눈이 다르면 출력할 것) -> check없이 출력
# M=3일 때는 순열(주사위 눈이 중복되는 경우 제외)  -> check 포함
# M=2일 때는 중복조합(눈의 전체 조합이 같으면 출력하지 말 것 - 하나의 출력에 눈의 중복은 나올 수 있다)
# 중복조합 for문 구현 - i -> j는 i부터 N까지 돌릴 것
# M=2의 경우 -> start를 파라미터로 넘겨야 한다
# M=4는 조합으로 만들기


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
        DFS_2(depth+1, i+1)   # 하나의 배열에 중복 숫자 제거하기

# 순열 - 중복 제거
def DFS_3(depth):

    if depth >= N:
        for i in range(N):
            print(record[i], end=" ")
        print()
        return

    for i in range(6):
        record[depth] = i+1
        DFS_3(depth+1)

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
record = [0] * N
check = [0] * N

if M == 1:
    DFS_1(0)
elif M == 2:
    DFS_2(0, 0)
elif M == 3:
    DFS_3(0)
elif M == 4:
    DFS_4(0, 0)

