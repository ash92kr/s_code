SIZE = 100
stack = [0] * SIZE   # 즉 0의 값을 가진 리스트 100개가 만들어진다 -> 값을 지워도 원래 값은 그대로 남아 있다
top = -1

def push(item):
    global top    # 전역변수화(value형은 이렇게 선언해주어야 넘긴다)
    if top > SIZE - 1:   # SIZE보다 작아야 한다
        return
    else:
        top += 1
        stack[top] = item    # reference형은 자동으로 넘어가므로 선언할 필요 없음

def pop():
    global top
    if top == -1:
        print('Stack is Empty!')
        return 0
    else:
        result = stack[top]
        top -= 1
        return result

push(1)
push(2)
push(3)
pop()
pop()   # 실제로 값이 지워지는 것은 아니다!!!
pop()
pop()



