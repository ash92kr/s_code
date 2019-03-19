import sys
sys.stdin = open("숫자 배열 회전_input.txt")

def rotate_90(array):

    global N

    new_array = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_array[j][N-1-i] = array[0][i][j]

    return new_array

def rotate_180(array):

    global N

    new_array = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_array[N-1-i][N-1-j] = array[0][i][j]

    return new_array


def rotate_270(array):

    global N

    new_array = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_array[N-1-j][i] = array[0][i][j]

    return new_array


T = int(input())

for tc in range(T):

    N = int(input())

    array = [[list(map(int, input().split())) for _ in range(N)]]


    array.append(rotate_90(array))
    array.append(rotate_180(array))
    array.append(rotate_270(array))

    print("#{}".format(tc+1))
    for i in range(N):  # 각 행이 먼저 나와야 한다
        for k in range(1, 4):   # k번째 면(0번째는 원본이므로 제외)
            if k != 1:   # 각 면을 시작할 때 공백을 주고 시작
                print(end=" ")
            for j in range(N):  # 각 열을 공백없이 출력한다
                print(array[k][i][j], end="")
        print()   # 각 줄이 끝나면 공백줄을 준다

