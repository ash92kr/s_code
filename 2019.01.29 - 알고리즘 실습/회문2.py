import sys
sys.stdin = open("회문2_input.txt")

for tc in range(10):

    N = int(input())
    data = [input() for _ in range(100)]

    max_length = 0
    palindrome = ""

    # 가로 방향으로 회문 구하기
    for i in range(len(data)):   # 행의 위치
        for j in range(100):   # 몇 개의 palindrome을 구할 것인가?
            for k in range(100-j+1):   # 시작점의 위치(j에 따라 시작점 개수가 유동적으로 바뀜)
                if data[i][k:k+j] == data[i][k:k+j][::-1]:
                    palindrome = data[i][k:k+j]
                if len(palindrome) > max_length:
                    max_length = len(palindrome)
                    # print(f'{palindrome}')

    # print(f'#{N} {palindrome}')

    # 세로 방향으로 회문 구하기
    data2 = []

    for i in range(len(data[0])):
        vertical = ""
        for j in range(len(data[i])):
            vertical += data[j][i]
        data2.append(vertical)

    for i in range(len(data2)):
        for j in range(100):
            for k in range(100-j+1):
                if data2[i][k:k+j] == data2[i][k:k+j][::-1]:
                    palindrome = data2[i][k:k+j]
                if len(palindrome) > max_length:
                    max_length = len(palindrome)
                    # print(f'{palindrome}')

    print(f'#{N} {max_length}')




