
# 그릇

# plate = list(map(str, input()))
#
# height = 10
# temp = plate[0]
#
# for i in range(1, len(plate)):
#     if temp == plate[i]:
#         height += 5
#     else:
#         height += 10
#     temp = plate[i]
#
# print(f'{height}')



# 전자레인지

# T = int(input())
#
# A = 0
# B = 0
# C = 0
#
# while True:
#
#     if T >= 300:
#         A = A + 1
#         T = T - 300
#     elif T >= 60 and T < 300:
#         B = B + 1
#         T = T - 60
#     elif T >= 10 and T < 60:
#         C = C + 1
#         T = T - 10
#     else:
#         break
#
# if T != 0:
#     print(-1)
# else:
#     print(f'{A} {B} {C}')




# 배부른 돼지

# n = int(input())
#
# food = []
#
# for i in range(n):
#     food.append(list(map(str, input().split())))
#
# times = 10
# not_good = 0
# temp_y = 0
# temp_n = 0
#
# for i in range(len(food)):
#     if food[i][1] == "Y":
#         temp_y = int(food[i][0])
#         if times > temp_y:
#             times = temp_y
#     else:
#         temp_n = int(food[i][0])
#         if not_good < temp_n:
#             not_good = temp_n
#
# if temp_n > times and times != 10:
#     print("F")
# elif times > 9 or times < 3:   # 문제를 잘 읽어야 한다!!!
#     print("F")
# else:
#     print(times)



# 배열 정리

Y, X = map(int, input().split())

matrix = []

for i in range(Y):
    matrix.append(list(map(int, input().split())))

# matrix = [[0, 1, 0, 0], [1, 1, 0, 1], [1, 0, 1, 0], [1, 1, 1, 0]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            for k in range(1, len(matrix[0])-j):
                if matrix[i][j+k] == 0:
                    break
                else:
                    matrix[i][j+k] = matrix[i][j+k-1] + 1

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()

