import sys
sys.stdin = open("스파이 조직_input.txt")

N, S = map(str, input().split())

arrow = []
spy = []
temp = ""

for i in S:
    if i == "<":
        arrow.append(i)
        spy.append(temp)  # 숫자가 아닌 경우에 다른 리스트에 넣음
        temp = ""
    elif i == ">":
        arrow.pop()
        spy.append(temp)
        temp = ""
    else:
        if len(arrow) == int(N):
            temp += i   # 다른 문자열 하나를 만들어서 숫자를 계속 더함

for j in range(len(spy)):
    if spy[j]:  # 순회하면서 "" 공백 문자열 삭제
        print(spy[j], end=" ")

