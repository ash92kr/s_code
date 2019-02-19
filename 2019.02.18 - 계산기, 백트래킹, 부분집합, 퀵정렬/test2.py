def process_solution(a, k):
    global cnt
    sum = 0
    for i in range(1, k+1):   # data = [1, 2, 3]이면 range(0, k)이다
        if a[i]:
            sum += data[i]

    if sum == 10:
        for i in range(1, k+1):   # 0번 인덱스는 사용하지 않음
            if a[i]:
                print(data[i], end=" ")
        print()
    cnt += 1

def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input):
    # 가지치기 후보 1
    global MAXCANDIDATES, total_cnt
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)  # 답이면 원하는 작업을 한다
    else:
        k += 1
        ncandidates = make_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            # 가지치기 후보 2
            backtrack(a, k, input)
    total_cnt += 1


MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * NMAX
cnt = 0
total_cnt = 0
backtrack(a, 0, 10)   # 10계층까지 내려가고 시작 계층(k)은 0

print(total_cnt)