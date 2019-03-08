import sys
sys.stdin = open("비밀금고_input.txt")

N = int(input())

num = list(map(int, input().split()))

array = [[0 for _ in range(2*N-1)] for _ in range(2*N-1)]

# start_x = 0
# start_y = len(array) // 2
line = 0   # 한 줄에서 몇 번 점을 찍어야 하는가?
idx = 0   # num에서 몇 번 값을 가져와야 하는가?

# for i in range(len(array)):
#     if i <= len(array) // 2:
#         line += 1
#     else:
#         line -= 1
#
#     if line % 2 == 0:
#         for j in range(line):
#             if j % 2 == 0:
#                 array[i][len(array)//2 + (2*(j//2)) + 1] = num[idx]
#             else:
#                 array[i][len(array)//2 - (2*(j//2)) - 1] = num[idx]
#             idx += 1
#     else:
#         for j in range(1, line+1):
#             if j % 2 == 0:
#                 array[i][len(array)//2 + (2*(j//2))] = num[idx]
#             else:
#                 array[i][len(array)//2 - (2*(j//2))] = num[idx]
#             idx += 1

# for문 하나로 풀기 = 시작점의 위치를 대상으로 +2씩 이동한다
for i in range(len(array)):
    if i <= len(array)//2:   # 중앙까지는 하나씩 증가해야 하고, 시작점의 열 위치는 하나씩 감소한다
        line += 1
        for j in range(line):   # (0, 3) (1, 2) (2, 1), (3, 0)
            array[i][len(array)//2 - i + (2*j)] = num[idx]
            idx += 1
    else:   # 중앙 다음 줄부터는 하나씩 감소해야 하고, 시작점의 열 위치는 하나씩 증가한다
        line -= 1
        for j in range(line):   # (4, 1) (5, 2) (6, 1)
            array[i][len(array)//2 - (len(array)-1-i) + (2*j)] = num[idx]
            idx += 1

# for i in range(len(array)):
#     print(i, array[i])

max_col = -987654321

# N이 아니라 array의 길이를 대상으로 열의 합을 구해야 한다
for i in range(len(array)):
    temp = 0
    for j in range(len(array)):
        temp += array[j][i]
    if temp > max_col:
        max_col = temp

print(max_col)

