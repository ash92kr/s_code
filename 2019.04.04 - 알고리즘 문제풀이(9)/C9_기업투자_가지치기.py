import sys
sys.stdin = open("C9_기업투자_input.txt")

def DFS(money):

    global profit

    # if money >= N:
    #     temp = 0
    #     if sum(record) == N:
    #         for i in range(M):
    #             temp += graph[record[i]][i+1]
    #         if temp > profit:
    #             profit = temp
    #     return
    #
    # for i in range(N):
    #     record[money] = i
    #     DFS(money + 1)



N, M = map(int, input().split())

graph = [[0] * (M+1)] + [list(map(int, input().split())) for _ in range(N)]

print(graph)

record = [0] * N

profit = 0

DFS(0)

print(profit)