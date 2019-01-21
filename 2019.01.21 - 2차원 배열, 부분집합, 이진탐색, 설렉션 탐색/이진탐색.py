def binarySearch(a, key):
    start = 0
    end = len(a) - 1

    while start <= end:
        middle = start + (end - start) // 2  # 가운데는 처음에서 끝을 뺀 값을 2로 나누어 정수만 취함

        if key == a[middle]:  # 검색 성공
            return middle
            # return True
        elif key < a[middle]:   # key보다 가운데 값이 큰 경우 끝을 가운데 -1한다
            end = middle - 1
        else:
            start = middle + 1   # key보다 가운데 값이 작은 경우 시작을 가운데 +1한다

    return -1

key = 22
data = [2, 4, 7, 9, 11, 29, 23]   # 반드시 정렬되어야 한다
print(binarySearch(data, key))