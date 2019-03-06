import sys
sys.stdin = open("호수의 깊이_input.txt")

N = int(input())

land = []

for i in range(N):
    land.append(list(map(int, input().split())))

depth = 0

for i in range(N):
    for j in range(N):
        left = 0
        right = 0
        up = 0
        down = 0
        if land[i][j] == 1:  # 현재 물이 있는 곳만 대상
            for k in range(j):  # 현재 기준점을 대상으로 왼쪽으로 이동
                if land[i][j-k] == 0:   # 0을 한번이라도 만나면 빠져나감
                    break
                else:
                    left += 1
            for k in range(N-j):  # 현재 기준점을 대상으로 오른쪽으로 이동
                if land[i][j+k] == 0:
                    break
                else:
                    right += 1
            for k in range(i):   # 현재 기준점을 대상으로 위로 이동
                if land[i-k][j] == 0:
                    break
                else:
                    up += 1
            for k in range(N-i):   # 현재 기준점을 대상으로 아래로 이동
                if land[i+k][j] == 0:
                    break
                else:
                    down += 1
            if min(left, right, up, down) != 0:   # 위 4개 거리 중 최소값이 0인 경우는 land에 대입하지 않음
                land[i][j] = min(left, right, up, down)   # 1 이상인 경우는

# 문제 잘못 이해
# idx = 0
#
# while True:
#
#     count = 0
#
#     for i in range(N):
#         for j in range(N):
#             if land[i][j] > idx:
#                 if land[i][j+1] > idx and land[i][j-1] > idx and land[i+1][j] > idx and land[i-1][j] > idx:
#                     land[i][j] += 1
#                     count += 1
#
#     idx += 1
#     if count == 0:
#         break

# print(land)

for i in range(N):
    for j in range(N):
        depth += land[i][j]

print(depth)