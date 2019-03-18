asc = [[0, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 1, 0, 0],
       [0, 1, 0, 1],
       [0, 1, 1, 0],
       [0, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 1],
       [1, 0, 1, 0],
       [1, 0, 1, 1],
       [1, 1, 0, 0],
       [1, 1, 0, 1],
       [1, 1, 1, 0],
       [1, 1, 1, 1]]   # 1부터 15까지의 숫자 코드

def aToh(c):   # 2진수 변환하기
    if c <= '9':
        return ord(c) - ord('0')   # 0~9는 0의 ascii코드를 기준
    else:
        return ord(c) - ord('A') + 10    # A~F는 A의 ascii코드를 기준 + 10추가

def makeT(x):
    for i in range(4):  #
        t.append(asc[x][i])

t = []
arr = "0F97A3"

for i in range(len(arr)):
    makeT(aToh(arr[i]))

n = 0
for i in range(len(t)):
    n = n * 2 + t[i]   # 2진수를 10진수로 변환
    if i % 7 == 6:   # 6자리면 출력하고 n 초기화
        print(n, end=", ")
        n = 0

if i % 7 != 6:   # 마지막 남은 3자리를 10진수로 바꾸고 초기화하기
    print(n)