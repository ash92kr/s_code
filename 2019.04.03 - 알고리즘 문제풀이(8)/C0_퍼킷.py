import sys
sys.stdin = open("C0_퍼킷_input.txt")

def DFS_mul(depth, mul):

    if depth >= N:
        s_mul.append(mul)
        return

    record[depth] = S[depth]
    DFS_mul(depth+1, mul*record[depth])

    record[depth] = 1
    DFS_mul(depth+1, mul)



def DFS_hap(depth, hap):

    if depth >= N:
        b_hab.append(hap)
        return

    record[depth] = B[depth]
    DFS_hap(depth+1, hap+record[depth])

    record[depth] = 0
    DFS_hap(depth+1, hap)


# 역시 순서가 중요하지 않아서 조합으로 풀어야 한다
# 곱의 합의 초기값은 1, 합의 초기값은 0을 준다
# depth 끝에 가면 0 ~ N개까지 선택한 모든 조합이 존재
# 아무 것도 선택하지 않은 경우의 최소값은 1이 자동으로 나온다 -> 예외값 처리 필요
# 각각의 함수에 count를 넣고 얼마나 섞었는가? 두 개의 초기값이 아무 것도 변하지 않은 경우 어떤 재료도 선택하지 않았다는 의미

N = int(input())

S = []
B = []

for i in range(N):
    s, b = map(int, input().split())
    S.append(s)
    B.append(b)

record = [0] * N
check = [0] * N

s_mul = []  # 조합의 곱을 담는 리스트
b_hab = []  # 조합의 합을 담는 리스트

DFS_hap(0, 0)
DFS_mul(0, 1)

# print(b_hab)
# print(s_mul)

sol = 987654321

for i in range(len(s_mul)-1):   # 마지막 값은 하나도 안 넣었을 때이므로 제외함
    if sol > abs(s_mul[i] - b_hab[i]):
        sol = abs(s_mul[i] - b_hab[i])

print(sol)