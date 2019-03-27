import sys
sys.stdin = open("전기카트_input.txt")

def perm(n, k, temp):

    global hab, data

    if temp > hab:  # 가지치기
        return

    if n == k:   # 최종층에 도착할 경우
        temp += data[idx[k-1]][idx[k]]   # data의 순열한 인덱스 k-1 ~ k(0)을 더한다
        if hab > temp:   # 만약 temp가 더 작은 경우, temp를 hab에 넣는다(최소합)
            hab = temp

    for i in range(k, n):   # 순열
        idx[i], idx[k] = idx[k], idx[i]
        perm(n, k+1, temp + data[idx[k-1]][idx[k]])   # temp + 순열한 값을 계속 넣는다
        idx[i], idx[k] = idx[k], idx[i]



T = int(input())

for tc in range(T):

    N = int(input())

    data = []

    for i in range(N):
        data.append(list(map(int, input().split())))

    hab = 987654321

    idx = [i for i in range(N)] + [0]  # 인덱스 리스트(마지막은 집=0)

    perm(N, 1, 0)   # 가장 마지막 0은 temp값, k=1단계부터 시작(집은 제외)

    print("#{} {}".format(tc+1, hab))


