# 짧게
s = "Reverse this strings"
s = s[-1::-1]
print(s)


# 길게
def my_strrev(ary):
    str = list(ary)   # 불변 형태를 가변 형태인 리스트로 변경
    for i in range(len(str)//2):
        t = ary[i]   # 임시 변수
        str[i] = str[len(str) - 1 - i]   # i번째에 -1-i번째의 값을 넣음
        str[len(ary) - 1 - i] = t   # 임시 변수의 값을 -1-i번째에 넣음
    ary = "".join(str)   # 리스트의 값을 다시 문자열로 합침
    return ary

ary = "abcde"
ary = my_strrev(ary)
print(ary)


