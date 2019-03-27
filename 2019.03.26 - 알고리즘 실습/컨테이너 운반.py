import sys
sys.stdin = open("컨테이너 운반_input.txt")

def bubble(data):

    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]


T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    weight = list(map(int, input().split()))

    truck = list(map(int, input().split()))

    bubble(weight)
    bubble(truck)

    memo = [[0 for _ in range(N)] for _ in range(M)]

    # 트럭 - 무게 테이블
    for i in range(N):
        for j in range(M):
            memo[j][i] = truck[j] - weight[i]

    sum = 0
    idx = []

    # for i in range(M):
    #     temp = 987654321
    #     for j in range(N):
    #         if memo[i][j] >= 0 and temp > memo[i][j]:
    #             if j not in idx:
    #                 temp = memo[i][j]
    #                 idx.pop()
    #                 idx.append(j)
    #
    #     if temp != 987654321:
    #         sum += truck[i] - temp

    # max로 지정되어 있어 처음부터 끝까지 순회하면서 짐을 실음
    for i in range(M):
        for j in range(i, N):
            if memo[i][j] >= 0 and j not in idx:   # 트럭의 무게가 남고 이전에 실은 짐이 아니면 sum에 더함
                sum += truck[i] - memo[i][j]
                idx.append(j)
                break

    # print(truck)
    # print(weight)
    # print(memo)

    print("#{} {}".format(tc+1, sum))

