import sys
sys.stdin = open("B2_주사위 던지기2_input.txt")

#
# def dice(no):   # X번째 주사위 -> depth : 주사위가 N+1이 되면 멈춰야 한다
#
#     if no > N:   # depth = no(no가 depth보다 크면 종료)
#         if sum == M:
#             print(sum)  #
#         return
#
#     for i in range(1, 7):  # 첫 번째 주사위 눈금 순회 -> 경우의 수를 모두 기록하면 끝냄 -> 주사위 눈을 모두 시도(순서를 고려하므로 순열)
#         if check[i]:   # check 되었다면 skip하기 -> 중복된 눈금 제거하기(1, 1 / 2, 2 등)
#             continue  # 그냥 순열 만들기 -> 처음부터 끝까지 모두 실시
#
#         check[i] = 1
#         record[no] = i   # 인덱스 번호를 저장(1번째 주사위에 1번 기록) # 이전 은행의
#         dice(no+1, sum + i)   # for문이 하나 더 돌아간다고 인식
#         check[i] = 0   # 해당 눈금에 0으로 표시함으로써 중복 순열 지우기
#
#         # 1번방 -> 2번방의 순으로 지속된다
#
#     # stack 인덱스는 1개씩 계속 증가 ->
#
#
#
# # 중복 순열
# N, M = map(int, input().split())
#
# # for i in range(1, 7):
# #     for j in range(1, 7):
# #         print(i, j)
# record = [0] * (7)
# check = [0] * (7)
#
# dice(N)


# 우선 중복순열부터
def DFS(number):

    if number > N:
        for i in range(1, N+1):
            print(record[i], end=" ")
        print()
        return

    for i in range(1, 7):
        record[number] = i
        DFS(number+1)

# 순열
def DFS2(number):

    if number > N:
        for i in range(1, N+1):
            print(record[i], end=" ")
        print()
        return

    for i in range(1, 7):  # 눈금
        if check[i]:
            continue
        check[i] = 1
        record[number] = i
        DFS2(number+1)
        check[i] = 0


def DFS3(number, hab):

    if number > N:
        if hab == M:
            for i in range(1, N+1):
                print(record[i], end=" ")   #
            print()
        return

    for i in range(1, 7):  # 눈금
        record[number] = i   # record의 인덱스에 i번 값을 넣는다
        DFS3(number+1, hab+i)   # hab은 이전까지의 합계이므로 갱신하면 안 된다(뒤의 파라미터는 내 것이 아니므로 갱신 금지)


# main -----------------
N, M = map(int, input().split())
record = [0] * 8   # 주사위별 눈 기록배열
check = [0] * 7   # 눈 사용여부 체크배열
# DFS(1)   # 첫 번째 주사위부터 시작
# DFS2(1)
DFS3(1, 0)   # 1번 주사위부터 시작, 합계는 0