import sys
sys.stdin = open("소수의 개수와 최대 최소 구하기_input.txt")

A, B = map(int, input().split())

# 에리토스테네스의 체
# sosu_A = [0] * (A+1)
# sosu_B = [0] * (B+1)

# for i in range(2, A+1):
#     if i * i > A:
#         break
#     if sosu_A[i] == 1:  # 예를 들어 4가 체크되었다면 4, 8 등은 체크할 필요 없다
#         continue
#     for j in range(i*2, A+1, i):   # i의 2배수부터 시작해서 A+1까지 i의 배수인지 확인한다
#         sosu_A[j] = 1   # 인덱스가 배열이므로 체크만 하고 넘어감
#
# for i in range(2, B+1):
#     if i * i > B:
#         break
#     if sosu_B[i] == 1:
#         continue
#     for j in range(i*2, B+1, i):
#         sosu_B[j] = 1

sieve = [0] * (100001)

for i in range(2, 100001):
    if i * i > 100000:
        break
    if sieve[i] == 1:
        continue
    for j in range(i*2, 100001, i):
        sieve[j] = 1

small = 0
big = 0

if A < B:
    small, big = A, B
else:
    small, big = B, A

sosu = []

for i in range(small, big+1):
    if sieve[i] == 0 and i != 1:    # 1은 소수에서 제외해야 한다
        sosu.append(i)

count = len(sosu)
hab = sosu[0] + sosu[-1]

print(count)
print(hab)
