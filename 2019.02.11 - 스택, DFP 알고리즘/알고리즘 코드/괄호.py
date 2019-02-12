def check(words):

    for i in words:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack != []:
                stack.pop()
                print(stack)
            else:
                print('left bracket is lack')
                return

    if len(stack) > 0:
        print('bracket is not equal!')
        return stack
    else:
        print('bracket is right')
        return


stack = []
# check('()()((()))')
# check('((()((((()()((()())((())))))')
# check('())')



s = list()
def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        print("stack is empty")
        return
    else:

        return s.pop(-1)

def isEmpty():
    if len(s) == 0:
        return True
    else:
        return False

def check_matching(data):
    for i in range(len(data)):
        if data[i] == "(":
            push(data[i])
        elif data[i] == ")":
            if isEmpty(): return False
            pop()

    if not isEmpty(): return False
    else: return True

data = input()
print(check_matching(data))
