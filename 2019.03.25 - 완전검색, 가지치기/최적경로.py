import sys
sys.stdin = open("최적경로_input.txt")

import time
# from time import strftime

start_time = time.time()

def check(n):

    global dist

    temp = 0

    for i in range(0, len(n), 2):
        if i == 0:
            temp += abs(start[0] - data[i]) + abs(start[1] - data[i+1])
        else:
            temp += abs(data[i-2] - data[i]) + abs(data[i-1] - data[i+1])

    temp += abs(end[0] - data[-2]) + abs(end[1] - data[-1])

    if temp < dist:
        dist = temp


def perm(n, k):

    if n == k:
        check(data)
    else:
        for i in range(k, N):
            data[(i*2)], data[(i*2)+1], data[(k*2)], data[(k*2)+1] = data[(k*2)], data[(k*2)+1], data[(i*2)], data[(i*2)+1]
            perm(n, k+1)
            data[(i*2)], data[(i*2)+1], data[(k*2)], data[(k*2)+1] = data[(k*2)], data[(k*2)+1], data[(i*2)], data[(i*2)+1]


T = int(input())

for tc in range(T):

    N = int(input())
    count = 0

    data = list(map(int, input().split()))

    start = []
    start.append(data.pop(0))
    start.append(data.pop(0))

    end = []
    end.append(data.pop(0))
    end.append(data.pop(0))

    dist = 987654321

    perm(N, 0)

    print("#{} {}".format(tc+1, dist))

print(time.time() - start_time, 'seconds')










