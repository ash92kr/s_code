import sys
sys.stdin = open("숫자 맞추기_input.txt")

N = int(input())

card = []

for i in range(N):
    card.append(list(map(int, input().split())))

score = [0] * N
double = []

for i in range(N-1):
    for j in range(i+1, N):
        for k in range(N):
            if card[i][k] == card[j][k]:
                double.append(card[j][i])
        if card[j][i] not in double:
            score[i] += card[j][i]
        else:
            double.pop()

print(score)

