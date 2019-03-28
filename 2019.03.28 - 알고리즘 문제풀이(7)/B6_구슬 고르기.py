# 0개부터 N개까지 고르는 조합
def DFS(number):

    if number >= N:
        for i in range(N):
            print(b[i], end=" ")
        print()
        return

    b[number] = a[number]  # 담기
    DFS(number+1)

    b[number] = 0
    DFS(number+1)

# N개 중 M개를 고르는 조합
def DFS2(number, count):

    if count == 2:
        for i in range(N):
            print(b[i], end=" ")
        print(count)
        return

    if number >= N:
        # if count == 2:
        #     for i in range(N):
        #         print(b[i], end=" ")
        #     print()
        #     return
        return

    b[number] = a[number]
    DFS2(number+1, count+1)

    b[number] = 0
    DFS2(number+1, count)



def DFS3(number, count):

    if count == 2:
        for i in range(N):
            print(b[i], end=" ")
        print(count)
        return

    if number >= N:
        return

    b[count] = a[number]   # 순서대로 담아야 한다
    DFS3(number+1, count+1)

    b[count] = 0
    DFS3(number+1, count)


# Main--------------------
a = [1, 2, 3]  # 구슬
b = [0, 0, 0]  # 구슬을 담을 상자
N = 3

DFS(0)
# DFS2(0, 0)
# DFS3(0, 0)

