import sys
sys.stdin = open("회전_input.txt")

def rotate(angle):

    global N, array, new_array

    if angle == 90:
        for i in range(N):
            for j in range(N):
                new_array[j][N-1-i] = array[i][j]

    elif angle == 180:
        for i in range(N):
            for j in range(N):
                new_array[N-1-i][N-1-j] = array[i][j]

    elif angle == 270:
        for i in range(N):
            for j in range(N):
                new_array[N-1-j][i] = array[i][j]

    # for i in range(N):
    #     for j in range(N):
            # print(new_array[i][j], end=" ")
            # array[i][j] = new_array[i][j]  # 배열 2개를 이용해 바꾼 값 저장하기
        # print()

    array = new_array

    for i in range(N):
        for j in range(N):
            print(new_array[i][j], end=" ")
        print()

N = int(input())

array = []

for i in range(N):
    array.append(list(map(int, input().split())))

new_array = [[0 for _ in range(N)] for _ in range(N)]

while True:

    angle = int(input())

    # if angle in [90, 180, 270, 360]:
    if angle == 90:
        rotate(angle)
    elif angle == 180:
        rotate(angle)
    elif angle == 270:
        rotate(angle)
    elif angle == 360:
        rotate(angle)

    if angle == 0:
        break



