import sys
sys.stdin = open("(2805)농작물 수확하기_input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    mid =  N // 2
    start = mid
    end = mid
    sum = 0
    for i in range(N):
        for j in range(start, end+1, 1):
            sum += data[i][j]
        if i < mid :
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print("#{} {}".format(tc, sum))

