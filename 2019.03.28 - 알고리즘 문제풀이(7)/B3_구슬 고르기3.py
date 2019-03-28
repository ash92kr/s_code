def DFS(number):  # 현재 no번째 상자에 모든 구슬을 순열구조로 담아보는 모든 경우

    # 1] 리턴조건 : 3개를 고른후 인쇄한 후 리턴
    if number == N:
        for i in range(N):
            print(b[i]+1, end=" ")
        print()
        return

    # 2] a배열에서 0요소부터 N전 요소전까지 고르는 모든 경우(단 구슬중복 배제)
    for i in range(N):

        if check[i]:
            continue
        check[i] = 1
        b[number] = i
        DFS(number+1)
        check[i] = 0

# main ============================
a = [1, 2, 3]  # 구슬
b = [0, 0, 0]  # 구슬을 담을 상자
check = [0, 0, 0]  # 구슬 사용여부 체크
N = 3

DFS(0) # b[0]요소부터 담기 시작
