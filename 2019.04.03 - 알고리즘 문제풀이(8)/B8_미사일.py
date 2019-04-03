import sys
sys.stdin = open("B8_미사일_input.txt")


# 현재 군함위치에서 반경이내 에너지 모두 차감
def clear(number):

    for i in range(N):  # 자기 자신을 포함해서 반경 안이라면 에너지 만큼 감소
        D = abs(ship[number][0] - ship[i][0]) + abs(ship[number][1] - ship[i][1])
        if D <= R:
            ship[i][2] -= P


# 현재 군함위치에서 반경이내 에너지 모두 복원
def restore(number):

    for i in range(N):
        D = abs(ship[number][0] - ship[i][0]) + abs(ship[number][1] - ship[i][1])
        if D <= R:
            ship[i][2] += P


def DFS(depth):   # 미사일을 반복해서 쏘아야 한다

    global min_ship

    if depth >= M:  # 가지의 끝에서 할 일
        
        count = 0  # 남아 있는 군함의 개수
        for i in range(N):
            if ship[i][2] > 0:   # 2차원 배열의 에너지가 0이상인 것만 남음
                count += 1

        if min_ship > count:
            min_ship = count
        return

    # 현재 미사일을 모든 군함에 쏘는 경우(군함이 침몰하지 않았으면 재시도)
    for i in range(N):
        if ship[i][2] <= 0:  # 침몰하면 시도 불가
            continue
        clear(i)   # i번째 군함을 넘김
        DFS(depth+1)
        restore(i)   # 돌아올 때 사용하는 함수 = 이것이 check함수의 역할(백트래킹)


# 군함의 중복허용 필요, 단 군함이 침몰한 경우는 가지치기할 것
# 미사일을 발사한 경우 군함에 어떤 영향이 끼치는지 계산하고, 침몰하면 제외하고 나머지 경우의 수에 넣을 것
# 다시 돌아온 경우, 에너지를 복원시켜주어야 한다 = check와 비슷한 개념이다
# 에너지 차감과 복원은 함수로 빼서 처리하는 것이 좋다


# 군함이 없는 바다에 발사된 미사일은 폭발범위 이내의 군함에 영향을 주지 못한다 = 문제 제대로 읽기
# 좌표와 에너지를 군함별로 넣어야 한다
# 복원할 때도 해당 범위 내에 있는 군함들의 에너지를 넣어야 한다


N = int(input())  # 군함 개수

ship = [list(map(int, input().split())) for _ in range(N)]  # 군함 좌표, 군함 에너지

M, P, R = map(int, input().split())  # 미사일 개수, 화력, 화력 범위

# for i in range(N):
#     pan[ship[i][0]][ship[i][1]] = ship[i][2]

min_ship = 16  # 최대 군함 개수

DFS(0)  # 1번 미사일부터 시작

print(min_ship)

# 어떤 것이 depth이고, 무엇을 조작해서, 어떻게 check나 복원할 것인지 참고하기