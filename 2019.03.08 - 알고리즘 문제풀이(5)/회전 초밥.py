import sys
sys.stdin = open("회전 초밥_input.txt")

N, d, k, c = map(int, input().split())

sushi = []

for i in range(N):
    sushi += list(map(int, input().split()))

max_count = 0
kind = [0] * 3001   # 체크 리스트는 처음에 한 번만 만듦

for i in range(N):
    for j in range(k):
        kind[sushi[(i+j) % N]] = 1   # kind에 넣을 필요 없이 무조건 1값 넣음
    if kind[c] == 0:   # 쿠폰을 먹지 않았으면 먹었다고 표시
        kind[c] = 1
    temp = 0
    for m in range(1, d+1):   # 1번 메뉴부터 d번 메뉴까지만 인덱스 검색
        temp += kind[m]   # 1이라고 체크되어 있으면 값을 더하고
        kind[m] = 0   # 0으로 바로 초기화함
    if temp > max_count:
        max_count = temp

print(max_count)




