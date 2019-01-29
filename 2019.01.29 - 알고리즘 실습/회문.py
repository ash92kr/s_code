import sys
sys.stdin = open("회문_input.txt")

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())   # N = 글자판 크기, M = 찾을 회문 길이
    finds = [input() for _ in range(N)]   # 글자판 크기만큼 str을 받아들임
                                          # (str도 sequence이므로 2차원 리스트를 적을 필요 없음)

    # print(finds)

    # 가로 방향으로 회문 구하기(구간합 참고)
    for i in range(len(finds)):    # 2차원 리스트의 문자열 개수만큼 반복
        for j in range(0, N-M+1):   # 하나의 행에서 N-M+1번 반복(N = M이면 1번도 반복하지 않으므로 +1을 함) -> 한 행에서 시작점(j)과 끝점(j+M-1)이 달라짐
            palindrome = ""    # 회문을 넣을 빈 문자열
            for k in range(int(M/2)):    # 각 시작 ~ 끝 부분에서 M/2번 반복해 회문 검사(k는 끝점에서 왼쪽으로 이동)        j+k j+M-1-k
                if finds[i][j+k] == finds[i][M-1-k+j]:    # i행의 j+k(시작점) ~ i행의 M-1-k+j(끝점)이 같은가?  ex) 0 ~ 12, 1 ~ 13, 2 ~ 14, 3 ~ 15
                    palindrome += finds[i][j+k]   # 회문의 절반을 문자열에 넣음
                if len(palindrome) == int(M/2):    # 전체 회문의 절반 길이에 다다르고
                    if M % 2 == 1:   # M이 홀수인 경우(13)
                        temp = palindrome   # 지금까지 저장한 내용을 temp 변수에 넣는다
                        palindrome += finds[i][j+int(M/2)]    # 회문 검사하지 않은 가운데 문자(j(시작점)+ int(M/2))를 추가
                        palindrome += temp[-1::-1]    # temp의 문자 역순으로 추가
                    else:
                        palindrome += palindrome[-1::-1]    # M이 짝수면 지금까지 넣은 문자열을 뒤집어서 추가
                    print(f'#{tc} {palindrome}')
                    break

    # 세로 방향으로 회문 구하기
    finds2 = []

    for i in range(len(finds[0])):    # 2차원 리스트의 열 방향 순회 참고
        vertical = ""
        for j in range(len(finds[i])):
            vertical += finds[j][i]
        finds2.append(vertical)

    # print(finds2)

    for i in range(len(finds2)):    # 이하의 내용은 가로 방향으로 회문 구하기와 똑같으므로 생략함
        for j in range(0, N-M+1):
            palindrome = ""
            for k in range(int(M/2)):
                if finds2[i][j+k] == finds2[i][M-1-k+j]:
                    palindrome += finds2[i][j+k]
                if len(palindrome) == int(M/2):
                    if M % 2 == 1:
                        temp = palindrome
                        palindrome += finds2[i][j+int(M/2)]
                        palindrome += temp[-1::-1]
                    else:
                        palindrome += palindrome[-1::-1]
                    print(f'#{tc} {palindrome}')
                    break