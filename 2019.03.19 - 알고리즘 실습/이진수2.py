import sys
sys.stdin = open("이진수2_input.txt")

T = int(input())

for tc in range(T):

    N = float(input())

    ten = []

    while len(ten) <= 12:  # 2씩 곱해나가면서 1 이상이면 1을 추가, 1보다 작으면 0 추가

        N *= 2

        if N >= 1:
            ten.append(1)
            N -= 1
        else:
            ten.append(0)

        if N == 0.0:
            break

    print("#{}".format(tc + 1), end=" ")
    if N == 0.0:
        for i in range(len(ten)):
            print("{}".format(ten[i]), end="")
        print()
    else:
        print("overflow")
