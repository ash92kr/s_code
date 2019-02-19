str1 = '2+3*4/5'   # 괄호가 없으면 우선순위를 고려할 필요 없음

op = []   # 연산자를 넣을 스택

str2 = ''

for i in str1:
    if i in ['+', '-', '*', '/']:
        op.append(i)
    else:
        str2 += i

for j in range(len(op)):
    str2 += op.pop()

print(str2)




str = "2+3*4/5"
stack = []

for i in range(len(str)):
    if str[i] == "+" or str[i] == "-" or str[i] == "*" or str[i] == "/":
        stack.append(str[i])
    else:
        print(str[i], end="")

while len(stack) != 0:
    print(stack.pop(), end="")




