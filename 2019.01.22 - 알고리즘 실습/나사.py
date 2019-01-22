import sys
sys.stdin = open("나사_input.txt")

T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    A = list(map(int, input().split()))
    B = []














    # min = A[1]
    #
    # for i in range(N):
    #     if A[(i*2)+1] < min:
    #         min = (i*2)+1
    #
    # print(min)
    #
    # B = []
    #
    # # if A[(j*2)+1] == A[min]:
    # B.append(A[min - 1])
    # B.append(A[min])
    # A.pop(min)
    # A.pop(min - 1)

    # one_number = 0
    # j = 0
    #
    # while j < len(A):
    #
    #     numbers = [0] * 10
    #
    #     for i in range(len(A)):
    #         if A[i]






        # if A[min] == A[2*i]:
        #     A[(2*i)], A[(2*i)+1], A[(min-1)], A[min] = A[min-1], A[min], A[(2*i)], A[(2*i)+1]

    # for k in range(N):
    #     if B[(2*k)+1] == A[(2*(k+1))]:
    #         B.append(A[2*(k+1)])
            # B.append(A[2*(k+2)])

    # print(A)

    # while True:
    #
    #
    #
    #     for k in range(N-1):
    #         if A[(2*k)+1] < A[2*(k+1)+1]:
    #             break


    # while True:
    #
    #     for i in range(N-1):
    #         for j in range(i+1, N):
    #             if A[(2*i)+1] == A[(2*j)]:
    #                 A[(2*i)], A[(2*i)+1], A[(2*j)], A[(2*j)+1] = A[(2*j)], A[(2*j)+1], A[(2*i)], A[(2*i)+1]
    #
    #     for k in range(N-1):
    #         for l in range(k+1, N):
    #             if A[(2*k)+1] < A[(2*l)+1]:
    #                 break



    # for j in range(int(len(A)/2)):
    #     if A[(2*j)-1] == B[(2*j)+1]:
    #         B.append(A[(2*j)])
    #         B.append(A[(2*j)+1])
    # print(B)





