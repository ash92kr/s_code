count = 0
N = 3
A = [0 for _ in range(N)]
data = [1, 2, 3]

def printSet(n):  # 이 곳에 들를 때마다 count를 1개씩 증가시킴

    global count

    count += 1
    print("%d : " % (count), end="")   # 생성되는 부분 배열의 갯수 출력
    for i in range(n):  # 각 부분 배열의 원소 출력
        if A[i] == 1:   # A[i]가 1이면 포함된 것으로 보고 출력한다
            print("%d " % data[i], end="")
    print()
    
    
def powerset(n, k):   # k는 단계(현재 depth), n은 원소의 개수(DFS와 비슷하게 하나로 내려감)

    if n == k:   # Basis part
        printSet(n)
    else:   # Inductive part
        A[k] = 1   # k번 요소 포함
        powerset(n, k+1)   # 다음 요소 포함 여부 결정
        A[k] = 0   # k번 요소 미포함
        powerset(n, k+1)   # 다음 요소 포함 여부 결정

powerset(N, 0)