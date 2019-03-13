def bino(n, k):

    B = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # 재귀없이 for문으로만 만들어 빠름
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]

    return B[n][k]


print(bino(52, 5))
