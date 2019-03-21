import sys
sys.stdin = open("스도쿠 검증_input.txt")

T = int(input())

for tc in range(T):

    data = []

    for i in range(9):
        data.append(list(map(int, input().split())))

    flag = 1

    for i in range(9):
        temp = []
        for j in range(9):
            if data[j][i] not in temp:
                temp.append(data[j][i])
            else:
                flag = 0
                break

    for i in range(9):
        temp = []
        for j in range(9):
            if data[i][j] not in temp:
                temp.append(data[i][j])
            else:
                flag = 0
                break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            for k in range(3):
                if data[i+k][j+k] not in temp:
                    temp.append(data[i+k][j+k])
                else:
                    flag = 0
                    break

    print("#{} {}".format(tc+1, flag))
