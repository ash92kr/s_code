import sys
sys.stdin = open("B4_최소의 합_input.txt")

# 열을 중복해서 모두 실시 가능
def DFS(number, hab):   # 현재 행에서 모든 열을 사용하는 경우의 수

    global min_temp

    if hab > min_temp:   # 가지치기(합이 min_temp를 초과할 경우 return)
        return

    if number >= N:
        # for i in range(N):   # 합과 값 출력하기
        #     print(record[i], end=' ')
        # print(hab)

        if hab < min_temp:   # 가지치기
            min_temp = hab
        return

    for i in range(N):   # 열
        record[number] = data[number][i]   # 고른 값을 기록함
        DFS(number+1, hab + data[number][i])


# 열의 중복을 배제한 순열
def DFS2(number, hab):

    global min_temp

    if hab > min_temp:
        return

    if number >= N:
        if hab < min_temp:
            min_temp = hab
        return

    for i in range(N):
        if check[i]:
            continue
        check[i] = 1
        record[i] = data[number][i]
        DFS2(number+1, hab + data[number][i])
        check[i] = 0


N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

record = [0] * N
check = [0] * N

min_temp = 987654321
DFS(0, 0)  # 0행부터 시작, 합계는 0
print(min_temp)


min_temp = 987654321
DFS2(0, 0)   # 중복된 열 불가
print(min_temp)


