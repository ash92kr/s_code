import sys
sys.stdin = open("행렬 찾기_input.txt")

T = int(input())

for tc in range(T):

    N = int(input())   # 행과 열 개수 받기

    chemical = [[0 for _ in range(N)] for _ in range(N)]   # 2차원 빈 리스트

    for i in range(N):
        chemical[i] = list(map(int, input().split()))   # 빈 리스트에 값 채우기

    answer = []   # 빈 리스트
    count_m = 0   # 행렬의 개수를 담는 변수

    # 행/열의 개수 및 행렬 개수 구하기
    for i in range(N):
        for j in range(N):
            if chemical[i][j] != 0:   # 2차원 리스트의 값이 0이 아닐 경우
                count_r = 0   # 행을 담는 변수
                count_c = 0   # 열을 담는 변수

                while True:

                    for k in range(i, N):   # 0이 아닌 지점의 가로 방향을 순회하면서
                        if chemical[k][j] != 0:
                            count_c += 1   # 0이 아닌 값들의 개수를 열 변수에 담음
                        else:
                            break   # 하나라도 0이 아닌 값이 있으면 행 순회 종료

                    for l in range(j, N):   # 0이 아닌 지점의 세로 방향을 순회하면서
                        if chemical[i][l] != 0:
                            count_r += 1   # 0이 아닌 값들의 개수를 행 변수에 담음
                        else:
                            break   # 하나라도 0이 아닌 값이 있으면 열 순회 종료

                    for m in range(i, i+count_c):   # 가장 처음의 0값이 아닌 좌표에서 +r행, +c열 만큼 이동하면서
                        for n in range(j, j+count_r):
                            chemical[m][n] = 0   # 0으로 변경(visited와 같은 역할)

                    count_m += 1   # 위의 모든 과정을 마치면 행렬의 개수를 +1 처리
                    answer.append((count_c, count_r))   # 또한 해당 행렬의 행과 열의 개수를 튜플로 담아 리스트에 넣음
                    break

    # 정렬하기 - 버블 정렬
    for n in range(0, len(answer)-1):
        for o in range(n, len(answer)):
            if (answer[n][0] * answer[n][1]) > (answer[o][0] * answer[o][1]):   # 2개 튜플의 [0]과 [1]을 곱한 값이 클수록 뒤로 이동
                answer[n], answer[o] = answer[o], answer[n]
            elif (answer[n][0] * answer[n][1]) == (answer[o][0] * answer[o][1]):   # 2개 튜플의 [0]과 [1]을 곱한 값이 같다면 행의 개수가 큰 것이 뒤로 이동
                if answer[n][0] > answer[o][0]:
                    answer[n], answer[o] = answer[o], answer[n]

    # 출력
    print(f'#{tc+1} {count_m}', end=" ")
    for p in range(len(answer)):
        print(f'{answer[p][0]} {answer[p][1]}', end=" ")
    print()
