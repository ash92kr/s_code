import sys
sys.stdin = open("원안의 마을_input.txt")

N = int(input())

town = []
for i in range(N):
    town.append(list(map(int, input())))

# 기지국의 좌표 구하기
base_x = 0
base_y = 0

for i in range(N):
    for j in range(N):
        if town[i][j] == 2:
            base_x = i
            base_y = j
            break

r = 0

# 기지국에서 가장 거리가 먼 마을 구하기
for i in range(N):
    for j in range(N):
        temp = 0
        if town[i][j] == 1:
            temp = ((base_x-i)**2 + (base_y-j)**2) ** (1/2)   # x, y 좌표를 제곱한 값을 루트로 나누기
            if r < temp:   # 최대값 저장하기
                r = temp

if r != int(r):   # 루트로 나누면 정수값이어도 int 타입이 아니므로
    r += 1   # int 타입과 값이 다르면 가장 가까운 정수값을 위해 +1을 한다

print(int(r))


