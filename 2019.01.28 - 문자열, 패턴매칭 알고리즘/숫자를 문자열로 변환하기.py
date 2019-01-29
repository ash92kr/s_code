def itoa(x):

    str = []   # 빈 리스트
    y = 0

    while True:
        y = x % 10   # 일의 자리를 떼냄
        str.append(chr(y + ord('0')))   # 숫자의 최소 ASCII 코드를 더한 값을 str 리스트에 넣음
        x //= 10   # x는 일의 자리를 뺀 값으로 나눔

        if x == 0: break

    str.reverse()   # 가장 먼저 들어간 값을 가장 마지막에 두기
    str = "".join(str)   # 리스트를 풀되, 리스트의 원소들을 str로 변환하기
    return str

x = 123
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))
