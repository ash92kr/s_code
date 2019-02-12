def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        print("Stack is Empty!")
        return
    else:
        return s.pop(-1)

s = []   # 아무 길이도 지정하지 않음

push(1)
push(2)
push(3)

print(pop())
print(pop())
print(pop())
