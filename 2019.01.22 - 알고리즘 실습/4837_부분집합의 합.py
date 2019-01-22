import sys
sys.stdin = open("부분집합_input.txt")

T = int(input())

for test_case in range(1, T+1):

    A = [_ for _ in range(1, 13)]   # 집합 생성

    N, K = map(int, input().split())
    count = 0   # 조건을 만족하는 부분 집합의 개수

    for i in range(1<<len(A)):   # 일단 모든 부분집합을 펼침
        plus = 0   # 부분 집합의 원소 합
        sub = 0   # 부분 집합의 원소 개수
        for j in range(len(A)):   # j도 A집합의 원소 개수만큼 반복
            if i & (1<<j):   # i를 이진수로 바꾸고, j를 왼쪽으로 이동하면서 1이면 출력
                plus += A[j]   # 원소 합 출력
                sub += 1   # 원소 개수 추가

        if plus == K and sub == N:
            count += 1

    print(f'#{test_case} {count}')






