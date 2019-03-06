import sys
sys.stdin = open("시간외 근무 수당_input.txt")

check = []

for i in range(5):
    check += map(float, input().split())

time = 0

for i in range(0, len(check), 2):
    if check[i+1] - check[i] - 1 <= 0:   # 초과근무 시간에서 1시간을 빼니 음수인 경우
        time += 0
    elif check[i+1] - check[i] - 1 >= 4:   # 초과근무 시간에서 1시간을 빼도 4시간 이상인 경우
        time += 4
    else:
        time += check[i+1] - check[i] - 1

money = 0

if time >= 15:   # 15시간 이상인 경우 5% 감산
    money = time * 2 * 5000 * 0.95
elif time <= 5:   # 5시간 이하인 경우 5% 증산
    money = time * 2 * 5000 * 1.05
else:
    money = time * 2 * 5000

print(int(money))
