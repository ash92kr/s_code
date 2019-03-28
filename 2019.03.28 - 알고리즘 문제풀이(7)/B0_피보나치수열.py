import sys
sys.stdin = open("B0_피보나치수열_input.txt")

def pibo(N):

    if N == 1 or N == 2:
        return 1
    else:
        if point[N] != 0:
            return point[N]
        else:
            point[N] = pibo(N-1) + pibo(N-2)   # 2의 n승만큼 재귀를 해야 한다
            return point[N]

    # 가지치기 - 왼쪽에서 시행한 값을 오른쪽에서 같은 값에 대해 재귀를 또 시행한다
    # return 위에 넣으면 된다
    # 참고 N이 10 ~ 16 정도면 굳이 안해도 된다

N = int(input())
point = [0] * (N+1)

print(pibo(N))