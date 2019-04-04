import sys
sys.stdin = open("C9_기업투자_input.txt")

# def DFS(depth, a_count, b_count):
def DFS(money):

    global profit

    if money >= N:
        # temp = graph[a_count][1] + graph[b_count][2]
        # if temp > profit:
        #     profit = temp
        # for i in range(N):
        #     print(record[i], end=" ")
        # print()
        temp = 0
        if sum(record) <= N:
            # for j in range(N):
            #     print(record[j], end=" ")
            # print()
            for i in range(M):
                temp += graph[record[i]][i+1]
            if temp > profit:
                profit = temp
        return

    # DFS(depth+1, a_count+1, b_count)
    # DFS(depth+1, a_count, b_count+1)
    # DFS(depth+1, a_count, b_count)

    for i in range(N):
        record[money] = i
        DFS(money+1)


N, M = map(int, input().split())

graph = [[0] * (M+1)] + [list(map(int, input().split())) for _ in range(N)]

# for i in range(N+1):
#     print(graph[i])

# print(graph)

record = [0] * N

profit = 0

# DFS(0, 0, 0)  # depth, a_count, b_count
DFS(0)

print(profit)