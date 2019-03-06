import sys
sys.stdin = open("회문1_input.txt")

for tc in range(10):

    N = int(input())

    matrix = []

    for i in range(8):
        matrix.append(list(map(str, input())))   # 문자열 받아들이기

    count = 0   # 회문 개수 세기

    # 가로 방향 순회
    for i in range(len(matrix)):   # 행
        for j in range(len(matrix)-N+1):   # 열 : 8-회문 구할 길이+1만큼 순회해야 함
            temp = 0  # 초기화
            for k in range(N//2):   # 회문은 좌우 한쌍씩 비교하면 되므로 N/2회 실시하면 됨(홀수 길이일 경우 가운데 비교 불필요)
                if matrix[i][j+k] == matrix[i][j+N-k-1]:   # 특정 기준점에서 회문 길이만큼 떨어진 문자열 비교(바깥쪽에서 안쪽으로 비교)
                    temp += 1
            if temp == N//2:  # temp가 N//2회 만큼 카운트되면 회문이라는 의미
                count += 1

    # 세로 방향 순회
    for i in range(len(matrix)):  # 열
        for j in range(len(matrix)-N+1):  # 행 : 마찬가지로 회문 구할 길이를 빼주어야 함
            temp = 0
            for k in range(N//2):  # 이하 내용 동일
                if matrix[j+k][i] == matrix[j+N-k-1][i]:
                    temp += 1
            if temp == N//2:
                count += 1

    print("#{} {}".format(tc+1, count))