def PrintArray():
    for i in range(len(arr)):
        print("%3d" % arr[i], end=" ")   # 원소별로 3칸 공백을 준다
    print()

def partition(a, l, r):   # 정렬할 리스트, 왼쪽, 오른쪽
    pivot = a[l]    # 시작점을 준다
    i = l
    j = r

    while i < j:   # i가 j보다 작을 때까지 실시
        while a[i] <= pivot:  # a[i]가 pivot보다 작을 때만 실시
            i += 1
            if i == r:   # 인덱스 이동하되 i == r이면 종료
                break
        while a[j] >= pivot:   # a[j]가 pivot보다 클 때만 실시
            j -= 1
            if j == l:   # 인덱스 이동하되 j == l이면 종료
                break
        if i < j:   # i가 j보다 작으면 교체
            a[i], a[j] = a[j], a[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j

def quicksort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        quicksort(a, low, pivot-1)
        quicksort(a, pivot+1, high)

arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 83]
PrintArray()
quicksort(arr, 0, len(arr)-1)  # len은 실제 배열 길이이므로 인덱스를 나타내기 위해 -1을 함
PrintArray()