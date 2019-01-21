# 2차원 배열에 25개 숫자로 채우고, 각 요소와 그 이웃한 요소와의 차의 절대값

# arr =
'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''

arr = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    arr[i] = list(map(int, input().split()))

print(arr)   # 2차원 리스트로 생성됨

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]   # dx과 dy를 하나씩 묶어서 기존 값에 대응
                     # (0, -1)이면 위로 한 칸 이동, (0, 1)이면 아래로 이동
                     # (-1, 0)이면 왼쪽으로 이동, (1, 0)이면 오른족으로 이동

sum = 0   # 초기값 지정

def isWall(x, y):  # 벽인지 확인하는 함수
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5: return True
    return False

def calAbs(y, x):   # 절대값 처리
    if y - x > 0: return y - x
    else: return x - y   # -값 붙인 경우

for x in range(len(arr)):
    for y in range(len(arr[x])):   # 행 우선 조회
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]   # y값에 dy를 적용한 리스트 생성
            if isWall(testX, testY) == False:  # 벽이 아니면 실행
                sum += calAbs(arr[y][x], arr[testY][testX])   # y부터 작성함

print(f'sum = {sum}')   # print("sum = {}".format(sum))
