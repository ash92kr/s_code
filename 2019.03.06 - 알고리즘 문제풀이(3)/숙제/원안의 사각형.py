R = int(input())

count = 0   # 점을 세기 위한 변수

# x와 y 모두 1, 1부터 시작한다
for x in range(1, R):
    for y in range(1, R):
        if (x**2 + y**2) ** (1/2) <= R:   # 원점과 (x, y)의 거리가 R보다 작은 경우만 카운트(피타고라스의 정리)
            count += 1

print(count*4)   # 사분면이므로 4를 곱함