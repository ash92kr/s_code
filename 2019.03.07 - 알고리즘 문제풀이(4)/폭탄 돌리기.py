import sys
sys.stdin = open("폭탄 돌리기_input.txt")

K = int(input())
N = int(input())

temp = []

for i in range(N):
    temp.append(list(map(str, input().split())))

T = []
Z = []

for i in range(N):
    T.append(int(temp[i][0]))
    Z.append(temp[i][1])

time = 0

for i in range(N):
    time += T[i]   # 우선 문제 푸는 시간부터 더함
    if time > 210:   # 시간이 210초가 넘으면 다음 사람으로 넘어가지 않음
        print(K)
        break
    if Z[i] == "T":   # T이면 다음 사람으로 넘어감, P/F면 계속 그 사람이 품
        K += 1
        if K == 9:   # K가 9가 되면 1번 사람으로 순회하도록 만듦
            K = 1

if time <= 210:   # 모든 문제를 풀어도 시간이 210초가 넘지 않으면 폭탄 가진 사람에게 폭탄이 터짐
    print(K)
