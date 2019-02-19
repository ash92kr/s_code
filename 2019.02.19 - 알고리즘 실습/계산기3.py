import sys
sys.stdin = open("계산기3_input.txt")

def bracket(stack):

    br = []
    num = 0

    for i in range(len(stack), 0, -1):
        if stack[i] == "(":
            br.append(stack[i])
            stack.pop()
        else:
            num = stack.pop()

            for j in range(len(br)):
                stack.append(br[j])

    return num


for tc in range(10):

    N = int(input())
    word = list(map(str, input()))

    stack = []

    for i in range(N):
        if word[i] == "(":
            stack.append(word[i])
        elif word[i] == ")":
            for j in range(len(stack), 0, -1):
                if stack[j] == "(":
                    stack.remove(stack[j])
                    break
        elif word[i] in ["+", "-", "*", "/"]:

            a = bracket(stack)
            b = bracket(stack)

            result = 0

            if word[i] == "+":
                result = int(b) + int(a)
            elif word[i] == "-":
                result = int(b) - int(a)
            elif word[i] == "*":
                result = int(b) * int(a)
            elif word[i] == "/":
                result = int(b) / int(a)

            stack.append(int(result))
        else:
            stack.append(int(word[i]))

    print(f'{tc} {stack.pop()}')


