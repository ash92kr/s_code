Size = 100
Q = [0] * Size  

front, rear = 0, 0   # 초기 인덱스값

def isFull():
    global front, rear
    return (rear+1) % len(Q) == front

def isEmpty():
    global front, rear
    return front == rear

def enQueue(item):
    global rear
    if isFull():
        print("do not enter!")
    else:
        rear = (rear+1) % len(Q)
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue empty!")
    else:
        front = (front+1) % len(Q)
        return Q[front]

enQueue(1)
enQueue(2)
enQueue(3)

print(deQueue())  
print(deQueue())   
print(deQueue())

enQueue(4)
print(deQueue())   # 계속해서 값을 넣었다 뺄 수 있다
