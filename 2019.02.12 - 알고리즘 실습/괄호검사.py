import sys
sys.stdin = open("괄호검사_input.txt")

def test(letter):

    left = []

    for i in letter:
        # 예외처리 - 아무 것도 left 스택에 없는데 닫는 괄호가 나오면 False
        if len(left) == 0 and i in [')', '}', ']']:
            return 0

        # 여는 괄호가 나오면 스택에 추가
        if i in ['(', '{', '[']:
            left.append(i)

        # 닫는 괄호가 나오되 짝지어 나오지 않으면 False, 짝지어 나오면 pop을 통해 제거
        if i in [')', '}', ']']:
            if left[-1] == '(' and i == ')':
                left.pop()
            elif left[-1] == '{' and i == '}':
                left.pop()
            elif left[-1] == '[' and i == ']':
                left.pop()
            else:
                return 0   # 0 = int(False)

    # 모든 처리를 마친 다음에 스택에 원소가 남았으면 False, 없으면 True를 반환
    if len(left) == 0:
        return 1
    else:
        return 0


T = int(input())

for tc in range(T):

    N = input()

    print(f'#{tc+1} {test(N)}')
