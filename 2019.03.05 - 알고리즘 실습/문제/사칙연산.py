import sys
sys.stdin = open("사칙연산_input.txt")

def calculate():

    global op, left, right, num

    for i in range(len(num)-1, 0, -1):   # num 배열을 역순으로 순회
        if num[i] == 0:   # num의 원소가 0이면 아직 계산되지 않았다는 의미
            if op[i] == '+':
                num[i] = num[left[i]] + num[right[i]]  # 자식 노드의 num값을 가져와 계산(num[i] X)
            elif op[i] == '-':
                num[i] = num[left[i]] - num[right[i]]
            elif op[i] == '*':
                num[i] = num[left[i]] * num[right[i]]
            elif op[i] == '/':
                num[i] = num[left[i]] / num[right[i]]

    return num   # 계산된 배열

for tc in range(10):

    N = int(input())

    op = [0] * (N+1)   # 연산자 배열
    left = [0] * (N+1)   # 왼쪽 자식 노드 배열
    right = [0] * (N+1)   # 오른쪽 자식 노드 배열
    num = [0] * (N+1)   # 숫자 배열

    for i in range(N):
        temp = list(map(str, input().split()))
        if temp[1] in ["+", "-", "*", "/"]:   # 0열은 노드 번호이므로 생략 -> 1열이 연산자면
            op[i+1] = temp[1]   # 연산자에 넣기
            left[i+1] = int(temp[2])   # 왼쪽 자식 노드에 넣기
            right[i+1] = int(temp[3])   # 오른쪽 자식 노드에 넣기
        else:   # 1열이 피연산자면(숫자면)
            num[i+1] = int(temp[1])   # 숫자에 넣기

    calculate()

    print("#{} {}".format(tc+1, int(num[1])))   # 계산 결과를 정수로 변경
