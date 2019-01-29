import sys
sys.stdin = open("문자열 비교_input.txt")

T = int(input())

for tc in range(1, T+1):

    pattern = input()
    total = input()

    j = 0   # pattern index
    i = 0   # total index

    match = False   # 패턴이 total에 있는지 확인하는 변수

    while True:

        if total[i] != pattern[j]:
            i = i - j   # i, j가 같아도 +1을 하므로 다음 칸부터 다시 비교
            j = -1

        i += 1  # if 문 통과 여부와 상관없이 1칸씩 증가
        j += 1

        if j == len(pattern):  # 인덱스 j가 pattern의 길이에 도달하면
            match = True       # 모든 패턴이 total에 있다는 뜻이므로 True로 변경
            break
        if i >= len(total):   # 인덱스 i가 total의 길이에 도달하면
            break             # 모든 패턴이 total에 없다는 뜻이므로 False 유지

    if match == False:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')



