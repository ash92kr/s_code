def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i = i + 1

    if i < n: return i
    else: return -1


    # for i in range(n):
    #     if a[i] == key:
    #         return i
    # return -1


data = [4, 7, 2, 29, 41, 69]
key = 20
print(sequentialSearch(data, len(data), key))