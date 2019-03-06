import sys
sys.stdin = open("사냥꾼_input.txt")


def shoot1(i, j):
    for k in range(max(i, j)):
        if mountain[i][j+1+k] in [2, 9]:
            mountain[i][j+1+k] = 9
        else:    # mountain[i][j+1+k] in [0, 1]
            break

def shoot2(i, j):
    for k in range(max(i, j)):
        if mountain[i+1+k][j] in [2, 9]:
            mountain[i+1+k][j] = 9
        else:
            break

def shoot3(i, j):
    for k in range(max(i, j)):
        if mountain[i][j-1-k] in [2, 9]:
            mountain[i][j-1-k] = 9
        else:
            break

def shoot4(i, j):
    for k in range(max(i, j)):
        if mountain[i-1-k][j] in [2, 9]:
            mountain[i-1-k][j] = 9
        else:
            break

def shoot5(i, j):
    for k in range(max(i, j)):
        if mountain[i-1-k][j-1-k] in [2, 9]:
            mountain[i-1-k][j-1-k] = 9
        else:
            break

def shoot6(i, j):
    for k in range(max(i, j)):
        if mountain[i-1-k][j+1+k] in [2, 9]:
            mountain[i-1-k][j+1+k] = 9
        else:
            break

def shoot7(i, j):
    for k in range(max(i, j)):
        if mountain[i+1+k][j-1-k] in [2, 9]:
            mountain[i+1+k][j-1-k] = 9
        else:
            break

def shoot8(i, j):
    for k in range(max(i, j)):
        if mountain[i+1+k][j+1+k] in [2, 9]:
            mountain[i+1+k][j+1+k] = 9
        else:
            break

def find():

    global N, mountain

    for i in range(1, N+1):
        for j in range(1, N+1):
            if mountain[i][j] == 1:
                shoot1(i, j)   # 오른쪽
                shoot2(i, j)   # 아래쪽
                shoot3(i, j)   # 왼쪽
                shoot4(i, j)   # 위쪽
                shoot5(i, j)   # 좌상단
                shoot6(i, j)   # 우상단
                shoot7(i, j)   # 좌하단
                shoot8(i, j)   # 우하단


N = int(input())

mountain = [[0] * (N+2) for _ in range(N+2)]   # 우선은 0로 채운다

for i in range(1, N+1):   # 세로 행 추가
    mountain[i] = [0] + list(map(int, input())) + [0]   # 1 ~ N+1행 사이에 데이터 추가

# for i in range(N+2):
#     print(i, mountain[i])

rabbit = 0
find()

for i in range(1, N+1):   # 배열을 순회하면서 9만 카운트
    for j in range(1, N+1):
        if mountain[i][j] == 9:
            rabbit += 1

print(rabbit)