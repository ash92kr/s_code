import sys
sys.stdin = open("도약_input.txt")

N = int(input())

flower = []
for i in range(N):
    flower.append(int(input()))
flower.sort()

count = 0

for i in range(N-2):   # 0번부터 N-2번이 시작점
    f_length = 0   # 첫 번째 점프 거리의 초기화
    for j in range(i+1, N-1):   # i+1번부터 N-1번이 정류점
        s_length = 0   # 두 번재 점프 거리의 초기화
        f_length = flower[j] - flower[i]   # 첫 번째 점프 거리
        for k in range(j+1, N):   # j+1번부터 끝까지가 도착점
            s_length = flower[k] - flower[j]  # 두 번째 점프 거리
            if s_length <= 2 * f_length and s_length >= f_length:  # 두 번째 거리가 첫 번째 거리와 같거나 2배 이하여야 한다
                count += 1

print(count)


