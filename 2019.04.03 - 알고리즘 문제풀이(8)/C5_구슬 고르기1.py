# 조합 - 같은 것을 선택할 수 없다
# N이 되는 곳에서만 출력하면 빈 경우의 수가 생기므로 depth에 들어가면서 출력되도록 한다
# depth의 역할이 count와 같다


a = [1, 2, 3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3

def DFS(no, start): # a[no]번째 구슬을 상자에 담거나 담지 않는 모든 경우

    # 1] 리턴조건 : N번째이면 인쇄후 리턴
    # if no >= N or start >= N:   # 이 방식은 가장 마지막에 남은 것을 앞으로 민다
    #     for i in range(N):
    #         print(b[i], end=" ")
    #     print()
    #     return

    for i in range(N):   # 들어갈 때마다 물어봐야 할 때도 있다
        print(b[i], end=" ")
    print()

    if no >= N or start >= N:
        return

    # 2] 현재 구슬을 고르기(b배열에 담기)
    for i in range(start, N):
        b[no] = a[i]
        DFS(no+1, i+1)  # i+1을 하면 중복 배제

    # 3] 현재 구슬을 고르지 않기(b배열에 담지 않기)
        b[no] = 0

# main ============================
DFS(0, 0) # a[0]요소 구슬부터 시작