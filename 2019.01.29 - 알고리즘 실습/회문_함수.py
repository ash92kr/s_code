import sys
sys.stdin = open("회문_input.txt")

T = int(input())

def pal(data, N, M):

    # 가로 방향으로 회문 구하기
    for i in range(len(data)):
        for j in range(N-M+1):
            if data[i][j:j+M] == data[i][j:j+M][::-1]:
                return data[i][j:j+M]

    # 세로 방향으로 회문 구하기
    data2 = []

    for i in range(len(data[0])):
        vertical = ""
        for j in range(len(data[i])):
            vertical += data[j][i]
        data2.append(vertical)

    for i in range(len(data2)):
        for j in range(N-M+1):
            if data2[i][j:j+M] == data2[i][j:j+M][::-1]:
                return data2[i][j:j+M]


for tc in range(1, T+1):

    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    print(f'#{tc} {pal(data, N, M)}')