def process_solution(a, k, cursum):
    global ans
    if ans > cursum : ans = cursum   # 마지막에도 한 번 체크

def make_candidates(a, k, input, c):  # 2-1-3과 같이 후보 만들기
    global N
    in_perm = [False] * (N+1)   # 방문했는지 확인하는 배열

    for i in range(1, k):   # 1부터 k-1까지만 실시
        in_perm[a[i]] = True   # 해당 자리를 사용하면 True로 바꿈(2를 사용했다고 가정)

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, input, cursum):
    global ans, N

    if ans < cursum : return   # 현재 합이 최소값보다 크면 pass처리(가지치기)
    c = [0] * (N+1)   # candidate(크기를 n+1로 한 이유는 0을 사용하지 않기 때문)

    if k == input:
        process_solution(a, k, cursum) #답이면 원하는 작업을 한다.
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input, cursum + data[k-1][a[k]-1])
            # 현재의 sum에 data의 값을 더한다(1부터 k와 a배열이 시작하므로 -1을 한다)

import sys
sys.stdin = open('배열최소합_input.txt', 'r')
T = int(input())
for tc in range(T):
    ans = 987654321
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    a = [0] * (N+1)
    backtrack(a, 0, N, 0)
    print(f"#{tc+1} {ans}")




