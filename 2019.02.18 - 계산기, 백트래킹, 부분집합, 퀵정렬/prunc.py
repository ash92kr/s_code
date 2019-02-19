def process_solution(a, k, sum):
    if sum != 10:
        return

    global cnt

    for i in range(1, k+1):   # data = [1, 2, 3]이면 range(0, k)이다
        if a[i]:
            print(data[i], end=" ")
    print()
    cnt += 1

def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input, sum):
    # 가지치기 후보 1 - 모든 원소의 합이 10보다 크면 안해도 됨
    if sum > 10:
        return

    global MAXCANDIDATES, total_cnt
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k, sum)  # 답이면 원하는 작업을 한다
    else:
        k += 1
        ncandidates = make_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            # 가지치기 후보 2
            if a[k]:  # a[k]가 1이면 sum에 data[k]를 더해준다
                backtrack(a, k, input, sum + data[k])
            else:   # a[k]가 0인 경우 = 우측으로 간다
                backtrack(a, k, input, sum)
    total_cnt += 1


MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * NMAX
cnt = 0
total_cnt = 0
backtrack(a, 0, 10, 0)   # 10계층까지 내려가고 시작 계층(k)은 0

print(cnt)
print(total_cnt)