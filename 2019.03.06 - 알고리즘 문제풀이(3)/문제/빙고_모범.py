import sys
sys.stdin = open("빙고_input.txt")

def find(num):
    for i in range(5):
        for j in range(5):
            if Barr[i][j] == num:
                Barr[i][j] = 0
                return

def Bingo():
    Crosum1, Crosum2 = 0, 0
    cnt = 0

    for i in range(5):
        Rsum, Csum = 0, 0
        for j in range(5):
            Rsum += Barr[i][j]
            Csum += Barr[j][i]
        if Rsum == 0: cnt += 1
        if Csum == 0: cnt += 1
        Crosum1 += Barr[i][i]
        Crosum2 += Barr[i][5-i-1]

    if Crosum1 == 0: cnt += 1
    if Crosum2 == 0: cnt += 1
    if cnt >= 3: return True  # 부등호 주의
    else: return False

Barr = []
for i in range(5):
    Barr.append(list(map(int, input().split())))

Carr = []
for i in range(5):
    Carr.append(list(map(int, input().split())))

for i in range(5):
    flag = 0
    for j in range(5):
        find(Barr[i][j])  # 해당 숫자를 찾아 지우기
        if Bingo() == True:   # 3줄의 빙고를 찾으면 탈출
            flag = 1
            break
    if flag == 1:
        break

print(i*5 + j+1)  # 사회자가 부른 횟수