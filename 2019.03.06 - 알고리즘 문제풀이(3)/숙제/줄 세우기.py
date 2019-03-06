import sys
sys.stdin = open("줄 세우기_input.txt")

N = int(input())
card = list(map(int, input().split()))

line = [1]   # 첫 번째 학생은 무조건 줄을 세운다
stack = []

for i in range(1, N):   # 그 다음 학생부터
    if card[i] == 0:   # 0번을 뽑으면 계속해서 뒤로 세움
        line.append(i+1)
    else:   # 0번이 아닌 카드를 뽑으면
        for j in range(card[i]):  # 그 횟수만큼 원래 줄에서 학생을 빼서 다른 스택에 넣은 다음,
            temp = line.pop()
            stack.append(temp)
        line.append(i+1)   # 원래 뒤에 섰던 학생을 앞으로 댕김
        for k in range(card[i]):   # 스택에 넣은 학생들을 다시 원래 순서로 세움
            temp = stack.pop()
            line.append(temp)

for i in range(len(line)):
    print(line[i], end=" ")
