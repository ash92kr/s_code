import sys

def find():
    s = []
    for i in range(len(code)):
        if code[i] == '+' or code[i] == '-' or code[i] == '/' or code[i] == '*':
            if len(s) >= 2:
                op2 = int(s.pop())
                op1 = int(s.pop())
                if code[i] == '+':
                    s.append(op1 + op2)
                elif code[i] == '-':
                    s.append(op1 - op2)
                elif code[i] == '*':
                    s.append(op1 * op2)
                elif code[i] == '/':
                    s.append(op1 // op2)   # 파이썬은 그냥 나누면 실수가 되므로 정수 사용해야 함
            else:
                return 'error'
        elif code[i] != ' ' and code[i] != '.':   # 숫자이면 push
            s.append(code[i])                     # elif code[i].isdigit():
        elif code[i] == '.':    # 연산자가 .이면 pop이다
            if len(s) == 1:   # 마지막 결과값은 1개여야 한다
                return s.pop()
            else:
                return 'error'


sys.stdin = open('Forth_input.txt', 'r')
T = int(input())

for tc in range(1, T + 1):
    code = list(input().split())

    print('#{} {}'.format(tc, find()))
