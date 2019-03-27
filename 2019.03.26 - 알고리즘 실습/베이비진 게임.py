import sys
sys.stdin = open("베이비진 게임_input.txt")


T = int(input())

for tc in range(T):

    card = list(map(int, input().split()))

    A = []
    B = []

    for i in range(12):
        if i % 2 == 0:   # A와 B를 구분해서 정리
            A.append(card[i])
        else:
            B.append(card[i])

    idx_a = -1
    idx_b = -1

    A.sort()   # 정렬
    B.sort()

    for i in range(4):
        temp = i
        if A[i] == A[i+1] == A[i+2]:  # triple
            idx_a = temp
        for j in range(i+1, 5):   # 7 8 8 9와 같이 가운데 숫자가 여러 개 있는 경우
            if A[i] + 1 == A[j] and A[j] + 1 == A[j+1]:   # run
                idx_a = temp

    # print(A)
    # print(B)

    for j in range(4):
        temp = j
        if B[j] == B[j+1] == B[j+2]:
            idx_b = temp
        for k in range(j+1, 5):
            if B[j] + 1 == B[k] and B[k] + 1 == B[k+1]:
                idx_b = temp

    if idx_a != -1 and idx_b == -1:   # 어느 한 쪽만 -1이 아닌 경우 그 쪽이 승리
        print("#{} 1".format(tc+1))
    elif idx_a == -1 and idx_b != -1:
        print("#{} 2".format(tc+1))
    elif idx_a != -1 and idx_b != -1:   # 둘 다 -1이 아닌 경우 승/무승부 기록
        if idx_a < idx_b:
            print("#{} 1".format(tc+1))
        elif idx_a > idx_b:
            print("#{} 2".format(tc+1))
        else:
            print("#{} 1".format(tc+1))
    else:   # 둘 다 -1인 경우 무승부
        print("#{} 0".format(tc+1))

