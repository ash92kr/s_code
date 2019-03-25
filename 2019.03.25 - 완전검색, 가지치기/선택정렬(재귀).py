def recselectionsort(A, s, e):   # 범위를 줄여나가는 방식으로 구현
    mini = s   # 시작점을 최소 좌표로 사용
    
    if s == e: return   # 시작점이 끝 점과 같으면 종료
    
    for j in range(s+1, e, 1):   # for문을 1개 없앰
        if A[j] < A[mini]:
            mini = j
    
    A[s], A[mini] = A[mini], A[s]
    
    recselectionsort(A, s+1, e)



# def SelectionSort(A):
# 
#     n = len(A)
#     for i in range(0, n-1):
#         min = i
#         for j in range(i+1, n):
#             if A[j] < A[min]:
#                 min = j
#         A[min], A[i] = A[i], A[min]



A = [2, 1, 3, 4, 5]
# SelectionSort(A)
recselectionsort(A, 0, len(A))
print(A)