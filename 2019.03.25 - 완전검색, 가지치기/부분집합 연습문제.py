data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = [0 for _ in range(len(data))]
N = len(data)
#
# def powerset(n, k):
#
#     if n == k:
#         sum = 0
#         for i in range(n):
#             if A[i] == 1:
#                 sum += data[i]
#
#         if sum == 10:
#             for i in range(n):
#                 if A[i] == 1:
#                     print("%d " % data[i], end="")
#             print()
#
#     else:
#         A[k] = 1
#         powerset(n, k+1)
#         A[k] = 0
#         powerset(n, k+1)


count = 0
total = 0

def printSet(n):

    global count
    sum = 0
    for i in range(n):
        if A[i] == 1:
            sum += data[i]

    if sum == 10:
        count += 1
        print("%d : " % count, end="")
        for i in range(n):
            if A[i] == 1:
                print("%d " % data[i], end="")
        print()


def powerset(n, k):

    global total
    total += 1
    if n == k:
        printSet(n)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)


powerset(N, 0)
print("호출횟수 : {}".format(total))
