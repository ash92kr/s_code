data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = [0 for _ in range(len(data))]
N = len(data)
count = 0
total = 0


def printSet(n, sum):

    global count

    if sum == 10:
        count += 1
        print("%d : " % count, end="")
        for i in range(n):
            if A[i] == 1:
                print("%d " % data[i], end="")
        print()


def powerset(n, k, sum):

    global total

    if sum > 10:  # sum이 10보다 크면 pass
        return

    total += 1

    if n == k:
        printSet(n, sum)
    else:
        A[k] = 1
        powerset(n, k+1, sum + data[k])
        A[k] = 0
        powerset(n, k+1, sum)


powerset(N, 0, 0)   # 매개변수로 sum을 넘겨서 처리하는 방법
print("호출횟수 : {}".format(total))