import sys
sys.stdin = open("같은 모양 찾기2_input.txt")

M = int(input())

arr = []

for i in range(M):
    arr.append(list(map(int, input())))

P = int(input())

pattern = []

for i in range(P):
    pattern.append(list(map(int, input())))



def check(i, j):

    for k in range(P):
        for l in range(P):
            if arr[i+k][j+l] != pattern[k][l]:
                return 0

    return 1

# 90도 회전
def check_90(i, j):

    for k in range(P):
        for l in range(P):
            if arr[i+k][j+l] != pattern[l][P-k-1]:
                return 0

    return 1


# 180도 회전
def check_180(i, j):

    for k in range(P):
        for l in range(P):
            if arr[i+k][j+l] != pattern[P-k-1][P-l-1]:
                return 0

    return 1

# 270도 회전
def check_270(i, j):

    for k in range(P):
        for l in range(P):
            if arr[i+k][j+l] != pattern[P-l-1][k]:
                return 0

    return 1



answer = 0

for i in range(M-P+1):   # 모눈종이의 시작행 제어
    for j in range(M-P+1):   # 모눈종이의 시작열 제어
        if check(i, j) == 1:
            answer += 1
        if check_90(i, j) == 1:
            answer += 1
        if check_180(i, j) == 1:
            answer += 1
        if check_270(i, j) == 1:
            answer += 1

print(answer)