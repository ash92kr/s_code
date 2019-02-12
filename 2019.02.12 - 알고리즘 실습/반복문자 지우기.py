import sys
sys.stdin = open("반복문자 지우기_input.txt")

T = int(input())

for tc in range(T):

    words = input()
    stack = []   # 빈 스택

    for i in range(len(words)):
        if len(stack) == 0:   # isEmpty 함수 = 스택에 원소가 하나도 없으면
            stack.append(words[i])   # 무조건 1개 원소를 추가한다
        else:    # 스택에 원소가 있으면
            if stack[-1] == words[i]:   # 스택의 마지막 원소와 words가 같으면 제거
                stack.pop()   # 스택의 원소와 words[i]의 값을 생략함
            else:   # 스택의 마지막 원소와 words[i]가 다르면 스택에 값을 추가함
                stack.append(words[i])

    print(f'#{tc+1} {len(stack)}')



