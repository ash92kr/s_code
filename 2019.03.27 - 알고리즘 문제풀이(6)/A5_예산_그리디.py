import sys
sys.stdin = open("예산_input.txt")

N = int(input())
data = list(map(int, input().split()))
M = int(input())

data.sort()  # 이진탐색에서는 sort가 필요하지 않다

temp = 0
money = 0


for i in range(N):
    if temp + (data[i] * (N-i)) <= M:
        temp += data[i]
        money = data[i]   # 모든 부분을 통과하면 가장 마지막 값을 배정하면 된다
    else:
        money = (M - temp) // (N - i)   # 특정 상한값이 넘으면 그 이상은 순회할 필요가 없다
        break

print(money)