import sys
sys.stdin = open("B7_더하기_input.txt")

def DFS(number, hab):

    global K, flag

    if hab > K:   # 가지치기
        return

    if hab == K:   # 가지치기(이 부분을 바깥으로 빼면 더 빠르게 끝냄)
        flag = "YES"
        return

    if flag == "YES":   # 중간에 yes가 뜨면 끝냄
        return

    # 앞으로 더할 값을 예상해도 K보다 작은 경우 가지치기가 가능하다 = depth별로 남아 있는 자연수들의 합 더하기

    if number >= N:
        for i in range(N):
            print(record[i], end=" ")
        print(hab)
        # if hab == K:
        #     flag = "YES"
        #     return   # 가지치기 - depth 끝에서 검증하기
        return

    record[number] = data[number]
    DFS(number+1, hab + data[number])

    record[number] = 0
    DFS(number+1, hab)


T = int(input())

for tc in range(T):

    N, K = map(int, input().split())

    data = list(map(int, input().split()))
    record = [0] * N

    flag = "NO"

    DFS(0, 0)

    print(flag)
