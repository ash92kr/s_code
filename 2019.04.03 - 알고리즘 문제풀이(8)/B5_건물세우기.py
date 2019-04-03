import sys
sys.stdin = open("B5_건물세우기_input.txt")

def DFS(number):

    global price

    if number >= N:
        temp = 0
        for i in range(N):
            temp += record[i]
        #     print(record[i], end=" ")
        # print()

        if price > temp:
            price = temp
        return

    for i in range(N):
        if check[i]:
            continue   # return이 아니라 continue
        record[number] = building[number][i]
        check[i] = 1
        DFS(number+1)
        check[i] = 0


N = int(input())

building = [list(map(int, input().split())) for _ in range(N)]

price = 987654321

check = [0] * N   # 어떤 장소를 사용했는가?

record = [0] * N   # 건물 비용을 넣음

DFS(0)

print(price)



