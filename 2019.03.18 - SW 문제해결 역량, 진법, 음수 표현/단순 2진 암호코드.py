import sys
sys.stdin = open("단순 2진 암호코드_input.txt")

def pattern(temp):

    global code, flag

    # arm = ['0001101', '0011001', '0010011', '0111101', '0100011',
    #        '0110001', '0101111', '0111011', '0110111', '0001011']

    # 역순
    arm = ['1011000', '1001100', '1100100', '1011110', '1100010',
           '1000110', '1111010', '1101110', '1110110', '1101000']

    for i in range(10):  # 10개 코드 중 하나라도 일치하면 그 때의 코드값 저장
        if temp == arm[i]:
            code.append(i)
            flag = 1

# 한 줄만 받아오기
def receive(send):

    for i in range(N):
        for j in range(M):
            if send[i][j] == 1:
                return i


T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    send = []

    for i in range(N):
        send.append(list(map(int, input())))

    # for i in range(N):
    #     print(i, send[i])

    code = []  # code를 담는 배열
    idx = M-1  # 인덱스로 사용하기 위해 초기값을 M-1로 설정

    start_x = receive(send)   # 어떤 줄을 받아올 것인가?

    while len(code) <= 7:   # 8개의 암호 코드를 받으면 종료

        flag = 0
        temp = ""

        for i in range(7):   # 숫자 7개를 문자열로 변환해서 합침
            temp += str(send[start_x][idx-i])

        pattern(temp)

        if flag:   # flag가 True면 7칸을 이동하고 False면 1칸을 이동
            idx -= 7
        else:
            idx -= 1


    catch = 0
    # print(code)

    for i in range(len(code)-1, 0, -1):  # 역순이므로 -1부터 1까지 조건에 맞게 더함
        if i % 2 == 1:
            catch += code[i] * 3
        else:
            catch += code[i]

    if (catch + code[0]) % 10 == 0:   # 가장 첫 값을 더한 값이 10의 배수면 sum출력, 아니면 0 출력
        print("#{} {}".format(tc+1, sum(code)))
    else:
        print("#{} 0".format(tc+1))