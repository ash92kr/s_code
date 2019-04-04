import sys
sys.stdin = open("C7_치킨배달2_input.txt")

def solve():

    temp = 0

    for i in range(len(house)//2):  # 현재 집에서 고른 치킨집과 최소인 거리 찾기
        min_house = 987654321
        for j in range(len(chick)//2):
            if not record[j]:   # 선택 안 한 치킨집이면 스킵(치킨집이므로 i가 아닌 j여야 한다)
                continue
            min_house = min(min_house, street[j][i])   # 최소거리
        temp += min_house

    return temp


def DFS(depth, count):

    global min_dis, N, M

    # M개를 골랐을 때의 치킨집과 최소의 거리합 비교
    if count == M:

        temp = solve()

        if min_dis > temp:
            min_dis = temp
        return

    if depth >= len(chick)//2:
        return

    # 현재 치킨집을 고르거나 고르지 않는 경우
    record[depth] = 1
    DFS(depth+1, count+1)

    record[depth] = 0
    DFS(depth+1, count)



N, M = map(int, input().split())   # N = 도시 크기, M = 남길 치킨집

road = [list(map(int, input().split())) for _ in range(N)]

# 치킨집을 행, 일반집을 열에 두는 정보 테이블 생성
# 그 다음, 치킨집을 조합으로 선택하는 방식
# 마지막으로 가지의 끝에서 치킨 거리의 최소값을 구하는 for문 사용

chick = []
house = []

for i in range(N):
    for j in range(N):
        if road[i][j] == 2:
            chick.append(i)
            chick.append(j)
        elif road[i][j] == 1:
            house.append(i)
            house.append(j)


street = []

for i in range(0, len(chick), 2):   # 행을 치킨집
    temp = []
    for j in range(0, len(house), 2):
        temp.append(abs(chick[i]-house[j]) + abs(chick[i+1]-house[j+1]))
    street.append(temp)

record = [0] * (len(chick)//2)   # house/chick의 길이만큼 record 배열을 만들어야 한다

min_dis = 987654321

DFS(0, 0)

print(min_dis)