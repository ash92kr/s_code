
def CountingSort(A, B, C):
    for i in range(len(A)):
        C[A[i]] += 1    # A[i]에 해당하는 값을 C의 인덱스에 +1씩 추가함

    for i in range(1, len(C)):
        C[i] += C[i-1]   # C[i+1]의 값은 C[i]의 누적 값에 자기자신의 값을 추가함

    for i in range(len(A)-1, -1, -1):  # 마지막부터 처음까지 시작함
        B[C[A[i]]-1] = A[i]   # A[i] 값을 C리스트 인덱스(0부터 시작하므로 -1)에 해당하는 위치의 B리스트에 넣는다
        C[A[i]] -= 1   # 이 부분이 없으면 B리스트의 계속 같은 위치에 A[i] 값이 들어간다

    return B

A = [1, 4, 5, 3, 8, 5, 3, 5, 6, 3]   # C와 마찬가지로 10개가 되어야 함
B = [0] * len(A)
C = [0] * 10  # 최대값 + 1

print(CountingSort(A, B, C))

