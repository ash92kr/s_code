import sys

sys.stdin = open("flatten_input.txt")

T = 10

for i in range(T):

    dump = int(input())
    height = list(map(int, input().split()))

    flatten = 0   # 평탄화 높이

    count = 0

    while True:

        for j in range(len(height)-1, 0, -1):
            for k in range(0, j):
                if height[k] > height[k+1]:
                    height[k], height[k+1] = height[k+1], height[k]

        height[0] += 1
        height[-1] -= 1

        count += 1
        flatten = height[-2] - height[1]
        # -1과 0은 각각 +1과 -1이 실행되었으므로 그 전과 그 후의 값으로 max-min을 구함

        if count == dump:
            break

    print(f'#{i+1} {flatten}')
