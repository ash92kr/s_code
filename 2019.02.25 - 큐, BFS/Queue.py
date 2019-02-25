Size = 100
Q = [0] * Size  # length를 0으로 채움

front, rear = -1, -1   # 인덱스 값

def isFull():
    global rear
    return rear == len(Q)-1

def isEmpty():
    global front, rear
    return front == rear

def enQueue(item):
    global rear
    if isFull():
        print("do not enter!")
    else:
        rear += 1
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue empty!")
    else:
        front += 1
        return Q[front]

def Qpeek():
    global front, rear
    if isEmpty():
        print("Queue empty!")
    else:
        return Q[front+1]


enQueue(1)
enQueue(2)

# print(deQueue())
# print(deQueue())

print(Q.pop(0))   # pop할 때 0번인지 확인(가장 앞쪽 원소를 빼야 하므로)
print(Q.pop(0))   # 선형 큐의 단점 : 앞 부분에 공간이 있어도 인덱스가 계속 뒤로 간다


if len(Q) != 0:   # front와 rear가 같다면 공백이라는 의미
    print(Q.pop(0))
print(Q)   # 리스트로 만들면 pull은 값을 확인하지 않는다