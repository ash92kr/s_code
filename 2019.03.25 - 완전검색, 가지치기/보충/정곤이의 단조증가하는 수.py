import sys
sys.stdin = open("정곤이의 단조증가하는 수_input.txt")

T = int(input())

for tc in range(T):

    N = int(input())

    data = list(map(int, input().split()))

    danjo = -1
    # 곱한 값이 단조인가?(뒷자리로 갈수록 수가 커져야 한다)

    for i in range(N-1):
        for j in range(i+1, N):
            temp = data[i] * data[j]
            if temp < 10:
                danjo = temp
            else:
                t = temp % 10   # 10으로 나눌 것(나머지)
                x = temp // 10   # 10으로 나눈 것의 몫
                flag = 1

                while x:
                    if x % 10 > t:   # 마지막 자리보다 이전 자리가 크면 false
                        flag = 0
                    t = x % 10
                    x = x // 10

                if flag:
                    if danjo < temp:
                        dango = temp

    print('# {} {}'.format(tc+1, dango))
                  