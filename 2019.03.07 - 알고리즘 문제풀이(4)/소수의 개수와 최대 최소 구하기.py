import sys
sys.stdin = open("소수의 개수와 최대 최소 구하기_input.txt")

def decimal(small, big):

    count = []

    for i in range(small, big+1):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            # count += 1
            count.append(i)

    a = len(count)
    b = count[0] + count[-1]

    print(a)
    print(b)


a, b = map(int, input().split())

if a < b:
    big = b
    small = a
else:
    big = a
    small = b

decimal(small, big)
