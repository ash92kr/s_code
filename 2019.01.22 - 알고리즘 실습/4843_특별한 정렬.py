import sys
sys.stdin = open("특별한 정렬_input.txt")

T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    a = list(map(int, input().split()))

    for i in range(0, N-1):
        least = i   # 최소값은 시작값인 i로 고정한다
        for j in range(i+1, N):
            if a[j] < a[least]:   # a[i]보다 작으면 대체
                least = j   # 최소값의 인덱스로 j를 설정
        a[i], a[least] = a[least], a[i]

    # sort_a = ""   # 문자열로 넣으면 숫자로 변환 불가
    sort_a = []   # 출력할 값을 넣을 리스트

    for k in range(N):
        if k % 2:  # k가 짝수면 False이므로 else로 들어가고, 홀수면 True이다
            # sort_a += f' {a[int(k/2)]}'
            sort_a.append(a[int(k/2)])   # k가 홀수면 2로 나누어 a[]의 앞쪽에서 인덱싱을 한다(1/3/5/7/9 -> 0/1/2/3/4)
        else:
            # sort_a += f' {a[int(-k/2) - 1]}'
            sort_a.append(a[int(-k/2) - 1])   # k가 짝수면 -를 붙여 a[]의 뒤쪽에서 인덱싱을 한다(0/2/4/6/8 -> -1/-2/-3/-4/-5)

    print(f'#{test_case} ', end="")

    for l in range(10):   # 앞의 10개만 출력한다
        print(sort_a[l], end=" ")
    print()

    # l = 0
    #
    # while l < len(sort_a):
    #
    #     if l == 0:
    #         print(f'#{test_case}', end=" ")
    #     print(sort_a[l], end=" ")
    #     l += 1
    # print()
