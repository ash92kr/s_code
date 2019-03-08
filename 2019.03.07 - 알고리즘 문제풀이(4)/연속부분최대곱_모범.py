import sys
sys.stdin = open("연속부분최대곱_input.txt")

N = int(input())

matrix = []

for i in range(N):
    matrix.append(float(input()))

max_mul = 0

# 2중 for문으로 구현하기 - 모든 경우의 수 고려
# for i in range(N):
#     temp = 1   # 초기화
#     for j in range(i, N):
#         temp *= matrix[j]   # 시작점부터 결과를 누적하면서
#         if temp > max_mul:   # 비교한다
#             max_mul = temp
#
# print("%.3f" % max_mul)   # round 함수를 사용하면 소수점이 0인 경우 삭제됨


# 1중 for문으로 구현하기

temp = 1

for i in range(N):
    # if temp * matrix[i] < matrix[i]:
    #     temp = matrix[i]
    # else:
    #     temp *= matrix[i]
    # if temp > max_mul:
    #     max_mul = temp

    temp *= matrix[i]   # 우선 곱한 다음에
    if temp < matrix[i]:   # 직전에 곱한 값이 시작점보다 작으면
        temp = matrix[i]   # 시작값을 초기화함(continue 역할)
    if temp > max_mul:   # 매번 max값과 비교함
        max_mul = temp


print("%.3f" % max_mul)   # round 함수를 사용하면 소수점이 0인 경우 삭제됨

