import sys
sys.stdin = open('파리 퇴치_input.txt')

# T = int(input())  # 테스트 케이스 개수
#
# for tc in range(T):
#
#     N, M = map(int, input().split())   # N행/N열 + M행/M열 부분 행렬
#
#     matrix = []   # 데이터를 받기 위한 빈 행렬
#
#     for i in range(N):
#         matrix.append(list(map(int, input().split())))
#
#     max_sum = 0   # 최대 sum값 담기 위한 변수
#
#     for i in range(N-M+1):   # N-M+1 : 전체 행에서 부분 행렬의 행을 뺀 다음 +1(시작점이 0이므로)
#         for j in range(N-M+1):   # list index out of range 에러 방지
#             sum_m = 0   # 부분 행렬의 합을 담는 변수
#             for k in range(M):   # 부분 행렬의 시작점
#                 for l in range(M):
#                     sum_m += matrix[i+k][j+l]   # k와 l은 0부터 시작하므로 부분 행렬의 합을 구할 수 있다
#             if sum_m > max_sum:
#                 max_sum = sum_m   # 최대 합보다 부분 행렬의 합이 큰 경우만 max_sum을 바꿈
#
#     print(f'#{tc+1} {max_sum}')


def sub_matrix(i, j):

    global max_sum

    sum_m = 0  # 부분 행렬의 합을 담는 변수

    for k in range(M):  # 부분 행렬의 시작점
        for l in range(M):
            sum_m += matrix[i+k][j+l]  # k와 l은 0부터 시작하므로 부분 행렬의 합을 구할 수 있다

    if sum_m > max_sum:
        max_sum = sum_m  # 최대 합보다 부분 행렬의 합이 큰 경우만 max_sum을 바꿈

    return max_sum


T = int(input())  # 테스트 케이스 개수

for tc in range(T):

    N, M = map(int, input().split())   # N행/N열 + M행/M열 부분 행렬

    matrix = []   # 데이터를 받기 위한 빈 행렬

    for i in range(N):
        matrix.append(list(map(int, input().split())))

    max_sum = 0  # 최대 sum값 담기 위한 변수

    for i in range(N-M+1):   # N-M+1 : 전체 행에서 부분 행렬의 행을 뺀 다음 +1(시작점이 0이므로)
        for j in range(N-M+1):   # list index out of range 에러 방지
            sub_matrix(i, j)   # 함수를 통해서 값을 받을 수도 있다(속도가 다소 느림)

    print(f'#{tc+1} {max_sum}')



# def get_sum(i, j):
#
#     global M
#
#     sum = 0
#
#     for x in range(M):
#         for y in range(M):
#             sum += data[i+x][j+y]
#     return sum

# max = 0
# min = 987654321
# for i in range(N-M+1):
#     for j in range(N-M+1):
#         sum = get_sum(i, j)
#             if max < sum: max = sum
#             if min > sum: min = sum
