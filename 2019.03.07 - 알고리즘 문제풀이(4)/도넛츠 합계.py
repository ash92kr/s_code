import sys
sys.stdin = open("도넛츠 합계_input.txt")

N, K = map(int, input().split())

matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

donut = 0

for i in range(K//2, N-K//2):
    for j in range(K//2, N-K//2):
        temp = 0
        for k in range(8):
            temp += matrix[i+dx[k]][j+dy[k]]
            if temp > donut:
                donut = temp

print(donut)
