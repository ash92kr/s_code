import sys
sys.stdin = open("빙고_input.txt")

def speak(num):

    global count, arr

    for i in range(len(arr)):   # 행과 열을 순회하면서 사회자가 부른 숫자를 0으로 지움
        for j in range(len(arr)):
            if arr[i][j] == num:
                arr[i][j] = 0
    count += 1

    return count


def bingo():

    global arr

    line = 0
    cross1sum = 0
    cross2sum = 0

    for i in range(5):
        rsum = 0
        csum = 0
        for j in range(5):
            rsum += arr[i][j]   # 가로의 합
            csum += arr[j][i]   # 세로의 합
        if rsum == 0:
            line += 1
        if csum == 0:
            line += 1
        cross1sum += arr[i][i]   # 대각선(우하향)의 합
        cross2sum += arr[i][5-i-1]   # 대각선(좌하향)의 합

    if cross1sum == 0:
        line += 1
    if cross2sum == 0:
        line += 1
    if line >= 3:   # 빙고가 3줄 이상이 한 번에 나올 수도 있으므로 3 이상을 체크
        return True

    return False


arr = [] * 5

for i in range(5):
    arr.append(list(map(int, input().split())))

answer = []

for i in range(5):
    answer += map(int, input().split())

count = 0
flag = 0

for i in range(25):
    speak(answer[i])
    flag = bingo()   # 함수의 return은 출력값이므로 그 값을 변수에 저장해야 한다

    if flag == 1:   # flag가 1이면 count 체크하고 break
        print(count)
        break
