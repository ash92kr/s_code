import sys
sys.stdin = open("색칠하기_input.txt")

T = int(input())

for test_case in range(1, T+1):

    arr = [[0 for _ in range(10)] for _ in range(10)]   # 빈 리스트 생성

    N = int(input())
    count = 0

    for i in range(N):

        r1, c1, r2, c2, color = map(int, input().split())   # 값 받기

        count = 0

        for j in range(r1, r2 + 1):   # 2차원 배열을 순회하는 행으로 r1, r2 지정
            for k in range(c1, c2 + 1):    # 2차원 배열을 순회하는 열로 c1, c2 지정
                arr[j][k] += color    # 색깔의 값을 더해줌

        # print(arr)

    for l in range(len(arr)):
        for m in range(len(arr[0])):
            if arr[l][m] == 3:   # 순회하면서 값이 셀의 값이 3인 개수 구하기
                count += 1

    print(f'#{test_case} {count}')
