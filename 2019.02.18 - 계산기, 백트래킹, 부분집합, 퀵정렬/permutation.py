# 부분집합과 동일
def process_solution(a, k):
    for i in range(1, k+1):
        if a[i]:
            print(data[a[i]], end=" ")
    print()

# 부분집합과 다름
def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX   # visited와 마찬가지로 in_perm[i]이 False인 것만 넣는다

    for i in range(1, k):   # 1부터 k(현재 깊이)까지 실시
        in_perm[a[i]] = True   # in_perm[a[1]] = True

    ncands = 0
    for i in range(1, input+1):   # 1부터 출력시작
        if in_perm[i] == False:
            c[ncands] = i    # c[ncands]에 1 이상의 값이 들어가면서 True가 됨
            ncands += 1   # 다음 인덱스로 넘어감
    return ncands

# 부분집합과 동일
def backtrack(a, k, input):
    # 가지치기1
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES   # 후보 리스트

    if k == input:   # k 계층이면 출력하기
        process_solution(a, k)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):   # 실제로 값을 출력하는 부분
            a[k] = c[i]
            # 가지치기2
            backtrack(a, k, input)

# 부분집합과 동일
MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * NMAX
backtrack(a, 0, 10)