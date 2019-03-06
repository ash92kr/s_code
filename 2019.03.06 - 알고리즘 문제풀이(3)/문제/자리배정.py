import sys
sys.stdin = open("자리배정_input.txt")

c, r = map(int, input().split())
K = int(input())

chair = [[0 for _ in range(r)] for _ in range(c)]

if c * r >= K:  # K가 c*r과 일치해도 계산 가능하다

    count = 0
    rows = r
    cols = c - 1   # 첫 행이 모두 채워지므로 첫 단계의 열의 개수는 -1을 한다
    x = 0
    y = -1   # 첫 시작은 (0, -1)에서 시작한 다음 +1을 해서 (0, 0)을 찍는다

    while count < c * r:

        for i in range(rows):  # 첫 시작은 행의 개수다(제발 그림 그려가면서 하자)
            y += 1
            count += 1
            chair[x][y] = count
        rows -= 1   # 그림을 그려보니 행과 열이 번갈아가면서 1번씩 감소하고 있다

        for i in range(cols):
            x += 1
            count += 1
            chair[x][y] = count
        cols -= 1

        for i in range(rows):
            y -= 1
            count += 1
            chair[x][y] = count
        rows -= 1

        for i in range(cols):
            x -= 1
            count += 1
            chair[x][y] = count
        cols -= 1

    # for i in range(c):
    #     print(chair[i])

    for i in range(c):  # 출력 방식
        for j in range(r):
            if chair[i][j] == K:
                print("{} {}".format(i+1, j+1))

else:
    print(0)