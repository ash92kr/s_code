import sys
sys.stdin = open("C1_테이프 이어 붙이기_input.txt")

def DFS(depth, count):

    global min_diff

    # if abs(temp1-temp2) > min_diff:
    #     return

    # if depth >= (N//2):
    #     temp1, temp2 = 0, 0
    #     for i in range(N):
    #         if i < (N//2):
    #             temp1 += record[i]
    #         else:
    #             temp2 += record[i]
    #
    #     if min_diff > abs(temp1 - temp2):
    #         min_diff = abs(temp1 - temp2)
    #     return

    # if depth >= (N//2):
    #     # temp = sum(record)
    #     temp = 0
    #     for i in range(N//2):
    #         temp += record[i]
    #     # if temp not in temp_sum:
    #     #     temp_sum.append(temp)
    #     if min_diff > abs(temp - (total_sum - temp)):
    #         min_diff = abs(temp - (total_sum - temp))
    #     return

    # for i in range(N):
    #     if check[i]:
    #         continue
    #     record[depth] = tape[i]
    #     check[i] = 1
    #     if depth < (len(tape)//2):
    #         DFS(depth+1, temp1+tape2[i], temp2)
    #     else:
    #         DFS(depth+1, temp1, temp2+tape2[i])
        # DFS(depth+1)
        # check[i] = 0

    if depth >= N:  # 일단 끝까지 가는 구문이 필요하다
        if count == (N//2):
            temp = 0
            for i in range(len(record)):
                temp += record[i]
            if min_diff > abs(temp - (total_sum - temp)):
                min_diff = abs(temp - (total_sum - temp))
        return  # 2개일 때 처리하고 나머지일 때는 return하는 방식이다

    record[depth] = tape[depth]
    DFS(depth+1, count+1)

    record[depth] = 0
    DFS(depth+1, count)


# N개 중에 M개를 고르는 조합 - 테이프의 전체 길이를 알 경우, 반만 고르면 나머지는 전체 합에서 빼면 길이가 나온다
# depth의 끝까지 갈 필요가 없다
# 가지치기 - 5개를 선택해야 하는데 현재 3개, 앞으로 1개 남은 상태에서는 합을 구할 필요가 없다
# index번호를 이용해서 계산(N - depth)

N = int(input())

tape = list(map(int, input().split()))

# tape2 = []
#
# for i in range(N):
#     if tape.count(tape[i]) == 1:
#         tape2.append(tape[i])

record = [0] * N
# check = [0] * N

min_diff = 987654321
total_sum = sum(tape)

DFS(0, 0)

print(min_diff)
