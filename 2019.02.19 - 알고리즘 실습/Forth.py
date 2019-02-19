import sys
sys.stdin = open('Forth_input.txt')

def post(code):
    for i in range(len(code)):
        if code[i] in ['+', '-', '*', '/']:
            if len(stack) < 2:   # 연산자를 만났을 때 숫자가 1개 이하라면 error
                return 'error'
            else:
                a = stack.pop()
                b = stack.pop()
                result = 0

                if code[i] == '+':   # str 연산자 처리
                    result = b + a
                if code[i] == '-':
                    result = b - a
                if code[i] == '*':
                    result = b * a
                if code[i] == '/':
                    result = b / a

                stack.append(int(result))   # stack에 넣을 때는 모두 int
        elif code[i] == '.':   # 가장 마지막까지 왔을 때 숫자가 2개 이상 있으면 에러
            if len(stack) > 2:
                return "error"
        else:
            stack.append(int(code[i]))   # stack에 넣을 때는 모두 int

    return stack.pop()


T = int(input())

for tc in range(T):

    code = list(map(str, input().split()))   # 값 받아오기

    stack = []   # 피연산자들을 담을 스택

    print(f'#{tc+1} {post(code)}')