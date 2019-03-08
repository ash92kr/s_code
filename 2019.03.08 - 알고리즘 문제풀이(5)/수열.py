import sys
sys.stdin = open("수열_input.txt")

N = int(input())
num = list(map(int, input().split()))

max_length = 0

start = num[0]
temp = 0

for i in range(1, N):
    if start <= num[i]:
        temp += 1
        start = num[i]
    else:
        temp = 0
        start = num[i]

max_length = temp



print(max_length)

