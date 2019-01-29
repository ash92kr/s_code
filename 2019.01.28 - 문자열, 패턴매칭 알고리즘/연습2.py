# 길게
def strcmp(str1, str2):
    i = 0
    if len(str1) != len(str2):  # 길이가 다르면 바로 False
        return False
    else:   # 길이가 같다면
        while i < len(str1) and i < len(str2):  # 무한 반복(인덱스는 문자열 길이보다 1 작음)
            if str1[i] != str2[i]:   # 2개 문자열의 문자가 다르면 False
                return False
            i += 1  # 계속 돌아감
    return True
    
a = "abc"
b = "abc"

print(strcmp(a, b))

# 짧게
print(a == b)
