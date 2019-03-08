import sys
sys.stdin = open("초콜릿 공장_input.txt")

N = int(input())

wrong = 0   # 오류의 가짓수(전역변수 처리)

for i in range(N):
    chocolate = list(map(str, input().split()))

    L = list(chocolate[0])
    H = list(chocolate[1])

    for j in range(len(L)-1):   # 첫 번째 공장에서 중복된 상품이 있는가?
        flag = 0
        for k in range(j+1, len(L)):
            if L[j] == L[k]:
                flag = 1
                wrong += 1
                break
        if flag == 1:
            break

    for j in range(len(H)-1):   # 두 번째 공장에서 중복된 상품이 있는가?
        flag = 0
        for k in range(j+1, len(H)):
            if H[j] == H[k]:
                flag = 1
                wrong += 1
                break
        if flag == 1:
            break

    equal = 0
    for j in range(len(L)):   # 각 공장의 제품에 중복된 상품이 3개 이상 있는가?
        flag = 0
        for k in range(len(H)):
            if L[j] == H[k]:
                equal += 1
                if equal >= 3:
                    wrong += 1
                    flag = 1
                    break
        if flag == 1:
            break

print(wrong)





