def atoi(string):
    value = 0
    i = 0
    while (i < len(string)):
        c = string[i]   # 가장 처음은 문자열
        if c >= '0' and c <= '9':   # 문자열도 아스키 코드로 크기 비교가 가능하다
            digit = ord(c) - ord('0')   # 숫자 문자열을 아스키 코드로 바꿈
        else:
            break
        value = (value * 10) + digit;   # 기존 value에 10을 곱해가면서 다음 자리 수를 더한다
        i += 1
    return value

a = '123'
print(type(a))
b = atoi(a)
print(type(b))
c = int(a)
print(type(c))

