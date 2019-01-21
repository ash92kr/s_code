# arr = [1, 2, 3]
# n = len(arr)

# for i in range(1 << n):
#     for j in range(n):
#         if i & (1 << j):
#             print(arr[j], end=",")
#     print()

arr = [-7, -3, -2, 5, 8]
n = len(arr)

for i in range(1 << n):

    hab = 0   # sum의 위치 초기화

    for j in range(n):
        if i & (1 << j):
            hab += arr[j]

    if hab == 0:
        for j in range(n + 1):
            if i & (1 << j):
                print(arr[j], end=" ")
        print()