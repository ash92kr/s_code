# n! 전용 알고리즘

def myprint(n):
    for i in range(n):
        print(" %d " % (a[i]), end="")
    print()

def perm(n, k):
    if n == k:   # 가장 하단부에 도달할 경우
        # myprint(n)   # 숫자를 출력한다
        print(a)
    else:
        for i in range(k, n):   # 현재 위치부터 최하층 위치(출력할 개수)에 도달할 때까지
            a[i], a[k] = a[k], a[i]   # 모든 원소값을 교체
            perm(n, k+1)   # DFS와 같이 최하층에 도달한 경우
            a[i], a[k] = a[k], a[i]   # 다시 원래대로 값 교체

# a = [1, 2, 3]
# perm(3, 0)

a = [70, 30, 10, 50, 90]
perm(5, 0)