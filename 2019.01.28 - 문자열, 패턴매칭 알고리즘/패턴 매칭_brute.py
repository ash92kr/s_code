p = "is"
t = "This is a book!"

# 구간합과 같이 for문 2개를 사용해도 된다


def bruteForce(text, pattern):
    ti = 0   # total text index
    pi = 0   # pattern index

    while ti < len(text) and pi < len(pattern):
        if text[ti] != pattern[pi]:
            ti = ti - pi
            pi = -1
        ti = ti + 1
        pi = pi + 1

    if pi == len(pattern):
        return ti - len(pattern)
    else:
        return -1

text = "TTTTAACCA"
pattern = "TTA"
print("{}".format(bruteForce(text, pattern)))


# 구간합
def bruteForce2(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:  # i부터 j를 더해 패턴이 일치하는가?
                break
            else:
                cnt += 1    # 일치하면 cnt를 추가한다
        if cnt >= len(pattern):   # 패턴 길이의 끝까지 가는 경우
            return i
    return -1

text = "This is a book. This is a computer."
pattern = "is"

print("{}".format(bruteForce2(text, pattern)))




# start = 0
# while True:
#     start = bruteForce(text, pattern, start)
#     print(start)
#     start = start + len(pattern)
#     if start > len(text) - len(pattern)

print(text.find(pattern))