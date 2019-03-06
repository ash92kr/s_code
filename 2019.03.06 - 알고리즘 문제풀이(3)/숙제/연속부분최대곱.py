import sys
sys.stdin = open("연속부분최대곱_input.txt")

N = int(input())

data = []

for i in range(N):
    data.append(float(input()))   # 실수로 숫자 받아들이기

max_mul = 0
temp = data[0]   # 시작점

for i in range(1, N):  # DP - memoization(이전에 사용한 값을 다시 사용하기 위한 방법)
    temp *= data[i]   # 시작점을 포함해서 부분곱을 실시
    temp = max(data[i], temp)   # 첫 번째 값과 temp 중 큰 값을 temp에 넣음(temp는 시작점에서 특정 점까지의 연속된 곱 중 최대값을 나타냄)
    max_mul = max(max_mul, temp)   # 최대곱과 temp 중 최대곱을 max_mul에 넣음

print("%.3f" % max_mul)