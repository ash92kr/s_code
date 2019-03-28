import sys
sys.stdin = open("A1_최소 비용으로 포장 다시 하기_input.txt")

N = int(input())
data = list(map(int, input().split()))

candy = 0

# 일반 정렬
for k in range(N-1):
    for i in range(k, k+2):   # 해당 위치에서 2개씩만 정렬
        for j in range(i+1, N):   # k는 다음 값보다 큰 경우 끝까지 이동 가능(하지만 1번만 이동함)
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]  # 큰 값을 뒤로 이동함
    data[k+1] += data[k]  # 이전 값과 다음 값이 정렬된 상태에서 이전 값을 다음 값에 누적함
    candy += data[k+1]   # 두 번째 값부터 끝까지의 값을 누적함(한 칸씩 이동하면서 누적됨)

print(candy)


# 삽입 정렬
data.sort()
for k in range(1, N):
    data[k] += data[k-1]
    candy += data[k]
    temp = data[k]
    for i in range(k+1, N):
        if data[i] < temp:
            data[i], data[i-1] = data[i-1], data[i]
        else:
            break

print(candy)


