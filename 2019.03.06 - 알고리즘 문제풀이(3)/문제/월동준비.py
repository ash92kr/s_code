import sys
sys.stdin = open("월동준비_input.txt")

N = int(input())

acorn = list(map(int, input().split()))

clever = 0
stupid = 0
clever_count = 0
stupid_count = 0

for i in range(len(acorn)):   # 똑똑한 다람쥐는 양수만 먹는다
    if acorn[i] >= 0:
        clever += acorn[i]
        clever_count += 1

if clever_count == 0:  # 그런데 양수가 하나도 없다면 음수 중 가장 큰 값만 먹는다
    max_acorn = -99999
    for i in range(len(acorn)):
        if max_acorn < acorn[i]:
            max_acorn = acorn[i]
    clever = max_acorn

temp = 0   # 멍청한 다람쥐는 연속해서 먹는다(1부터 시작해야
for i in range(0, len(acorn)):
    temp += acorn[i]
    temp = max(acorn[i], temp)
    stupid = max(stupid, temp)
    if stupid > 0:
        stupid_count = 1

if stupid_count == 0:
    max_acorn = -99999
    for i in range(len(acorn)):
        if max_acorn < acorn[i]:
            max_acorn = acorn[i]
    stupid = max_acorn

print("{} {}".format(stupid, clever))
