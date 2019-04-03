def DFS(no):

    if no >= N:  # 3개 중 2개만 고르기(N 대신 2를 넣고 실시)
        for i in range(N):
            print(b[i], end=" ")
        print()
        return   # 더 이상 구슬을 넣을 공간이 없어 돌아감


    for i in range(N):
        if chk[i]:   # 사용했는지 여부 체크
            continue
        b[no] = a[i]   # b배열에 a에 있는 구슬들을 넣음 -> 나중에 return할 때는
        chk[i] = 1   # chk는 구슬을 넣은 공간에 체크 표시한다
        DFS(no+1)  # no는 구슬 몇 개를 담을까에 대한 변수
        chk[i] = 0  # 모든 구슬을 넣었다면 다시 돌아왔을 때 풀어주어야 한다
        # b[no] = 0  # 지울지 여부는 선택


a = [1, 2, 3]
b = [0, 0, 0]
chk = [0, 0, 0]
N = 3

DFS(0)
