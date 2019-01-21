def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]  # 교환하기

data = [49, 20, 109, 37, 56, 32, 11]
selectionSort(data)
print(data)
