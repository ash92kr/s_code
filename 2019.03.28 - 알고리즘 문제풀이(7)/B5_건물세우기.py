import sys
sys.stdin = open("B5_건물세우기_input.txt")

def DFS(number, hab):

    global min_temp

    if hab > min_temp:
        return

    if number >= N:
        if min_temp > hab:
            min_temp = hab
        return

    for i in range(N):
        if check[i]:
            continue
        check[i] = 1
        record[i] = data[number][i]
        DFS(number + 1, hab + data[number][i])
        check[i] = 0


N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]
record = [0] * N
check = [0] * N

min_temp = 987654321

DFS(0, 0)

print(min_temp)
