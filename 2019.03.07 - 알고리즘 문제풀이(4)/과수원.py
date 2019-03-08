import sys
sys.stdin = open("과수원_input.txt")

def apple(i, j):

    global left, right, up, down, farm

    for k in range(i):   # 0~i번 만큼 순회
        for l in range(j):
            up += farm[k][l]

    for m in range(i):
        for n in range(j, N):   # j~끝까지 순회
            right += farm[m][n]

    for o in range(i, N):   # i~끝까지 순회
        for p in range(j):
            left += farm[o][p]

    for q in range(i, N):   # 반복횟수는 자동으로 정해지므로 N을 사용해야 한다
        for r in range(j, N):
            down += farm[q][r]

    # print(left, right, up, down)

    return left, right, up, down   # 각 방향으로 더한 값을 return함

N = int(input())

farm = []

for i in range(N):
    farm.append(list(map(int, input())))

count = 0

for i in range(1, N):
    for j in range(1, N):  # 중심점의 좌표를 1, 1부터 5, 5까지로 봄
        left = 0   # 초기화는 매번 실시해야 한다
        right = 0
        up = 0
        down = 0
        apple(i, j)   # i, j번째 중심점을 기준으로 순회한다
        if left == right == up == down:   # 모든 방향의 합이 같으면 올바르게 나눈 경우
            count += 1

if count == 0:
    print(-1)
else:
    print(count)
