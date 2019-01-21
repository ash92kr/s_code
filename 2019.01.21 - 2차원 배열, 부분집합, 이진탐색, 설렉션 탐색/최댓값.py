import sys
sys.stdin = open("max_input.txt")

for test_case in range(1, 11):

    N = int(input())
    arr = [[0 for i in range(100)] for i in range(100)]

    for j in range(100):
        arr[j] = list(map(int, input().split()))

    sum = 0
    sum_list = []

    for k in range(len(arr)):
        for l in range(len(arr[k])):
            sum += arr[k][l]
        sum_list.append(sum)
        sum = 0

    for k in range(len(arr[0])):   # 0행의 열 개수
        for l in range(len(arr)):   # 행 개수
            sum += arr[l][k]   # arr[행][열]
        sum_list.append(sum)
        sum = 0

    for k in range(len(arr)):
        sum += arr[k][k]   # 우하향 대각선 합
        sum_list.append(sum)

    sum = 0

    for k in range(len(arr)):
        sum += arr[k][99-k]   # 좌하향 대각선 합
        sum_list.append(sum)

    # print(sum_list)
    max_sum = 0

    for m in range(len(sum_list)):
        if sum_list[m] > max_sum:
            max_sum = sum_list[m]

    print(f'#{test_case} {max_sum}')