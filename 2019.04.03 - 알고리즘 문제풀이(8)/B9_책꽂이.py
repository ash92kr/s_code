import sys
sys.stdin = open("B9_책꽂이_input.txt")

def DFS(number, hab):

    global min_diff, B

    # if hab < B:
    #     return

    if number >= N:
        if min_diff > (hab - B) and (hab - B) > -1:
            min_diff = (hab - B)
        return

    record[number] = height[number]
    DFS(number+1, hab + record[number])

    record[number] = 0
    DFS(number+1, hab)

# 고르고 고르지 않는 선택에 따라 경우의 수를 가지고 선택함
# 소들을 세워보고 높이를 정함 -> 순서는 상관없음(세워놓으면 되니까)
# 각 소들의 높이를 더할지 더하지 않을지에 따라 선택 -> 이중재귀
# 조합은 경우의 수가 많지 않다(2^n승) <-> 순열은 경우의 수가 많다

T = int(input())

for tc in range(T):

    N, B = map(int, input().split())

    height = [int(input()) for _ in range(N)]

    record = [0] * N

    check = [0] * N

    min_diff = 987654321

    DFS(0, 0)

    print(min_diff)
