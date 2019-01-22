import sys
sys.stdin = open("이진탐색_input.txt")

T = int(input())

for test_case in range(1, T+1):

    P, A, B = map(int, input().split())
    
    # 초기화
    start = 1
    end = P  # 정의하지 않아도 됨
    mid = int((start + end) / 2)

    count_A = 1   # A가 페이지를 찾은 횟수
    count_B = 1   # B가 페이지를 찾은 횟수

    while mid != A:
        if mid < A:
            start = mid   # 시작값을 mid로 대치
            # end = end
            mid = int((start + end) / 2)
        elif mid > A:
            # start = 1
            end = mid
            mid = int((start + end) / 2)

        count_A += 1
    
    # 초기화
    start = 1   
    end = P 
    mid = int((start + end) / 2)

    while mid != B:
        if mid < B:
            start = mid
            # end = end
            mid = int((start + end) / 2)
        elif mid > B:
            # start = 1
            end = mid
            mid = int((start + end) / 2)

        count_B += 1

    if count_A < count_B:
        print(f'#{test_case} A')
    elif count_A > count_B:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} 0')








