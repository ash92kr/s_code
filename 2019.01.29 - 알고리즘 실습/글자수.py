import sys
sys.stdin = open("글자수_input.txt")

T = int(input())

for tc in range(1, T+1):

    str1 = input()   # pattern
    str2 = input()   # total

    p_dict = { i: 0 for i in str1 }   # pattern에 있는 문자들을 key로 dict에 넣음
    # p_dict = { str1[i]: 0 for i in range(len(str1)) }

    for i in range(len(str2)):
        if str2[i] in p_dict.keys():   # total에 있는 문자가 p_dict에 있으면
            p_dict[str2[i]] += 1    # p_dict에 1 추가

    max_p = 0
    for j in p_dict.keys():   # p_dict에서 가장 value가 큰 값을 구함
        if p_dict[j] > max_p:
            max_p = p_dict[j]

    print(f'#{tc} {max_p}')