import sys
sys.stdin = open("종이붙이기_input.txt")

def logic(N):

    if N == 10:   # 홀수인 경우 최소값
        return 1

    if N == 20:   # 짝수인 경우 최소값
        return 3

    if (N // 10) % 2 == 1:   # N을 10으로 나눈 경우의 몫을 2로 나눈 나머지가 홀수인 경우
        return logic(N-20) * 4 + 1    # 10 = 1, 30 = 5, 50 = 21, 70 = 85와 같이 점화식이 4n+1
    else:   # N // 10이 짝수인 경우
        return logic(N-20) * 4 - 1    # 20 = 3, 40 = 11, 60 = 43과 같이 점화식은 4n-1

T = int(input())

for tc in range(T):

    N = int(input())

    print(f'#{tc+1} {logic(N)}')
