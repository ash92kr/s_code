
# 숫자근 - 입력 데이터 뒤에 공백 존재(int화)

# N = int(input())
#
# data = []
# for i in range(N):
#     data.append(list(map(str, input().split())))
#
# solution = 0
# max_root = 0
#
# while True:
#
#     root = 0
#
#     for i in range(len(data)):
#         for j in range(len(data[i])):
#             root += int(data[i][j])
#
#             if root >= 0 and root <= 9:
#                 if root > max_root:
#                     max_root = root
#                     break
#             else:
#                 while True:



# 색종이(초)

# N = int(input())
#
# paper = []
#
# for i in range(N):
#     paper.append(list(map(int, input().split())))
#
# array = [[0 for _ in range(100)] for _ in range(100)]
#
# for i in range(10):
#     for j in range(10):
#         for k in range(len(paper)):
#             array[paper[k][0]+i][paper[k][1]+j] = 1
#
# count = 0
#
# for i in range(len(array)):
#     for j in range(len(array[0])):
#         if array[i][j] == 1:
#             count += 1
#
# print(count)



# 색종이(중)
#
# N = int(input())
#
# paper = []
#
# for i in range(N):
#     paper.append(list(map(int, input().split())))
#
# array = [[0 for _ in range(110)] for _ in range(110)]  # 배열은 여유롭게 만들기 - 한번에 해결!
#
# for i in range(10):
#     for j in range(10):
#         for k in range(len(paper)):
#             array[paper[k][0]+i][paper[k][1]+j] = 1
#
# count = 0

# 배열은 항상 경계점을 신경써야 한다
# for i in range(110):
#     for j in range(110):
#         if array[i][j] == 1 and (i != 0 and j != 0):
#             if array[i-1][j] == 0:   # 상
#                 count += 1
#             if array[i+1][j] == 0:   # 하
#                 count += 1
#             if array[i][j-1] == 0:   # 좌
#                 count += 1
#             if array[i][j+1] == 0:   # 우
#                 count += 1


# 경계점에 1이 위치한 경우 사용
# for i in range(len(array)):
#     if array[0][i] == 1:
#         count += 1
#     if array[i][0] == 1:
#         count += 1
#     if array[len(array)-1][i] == 1:
#         count += 1
#     if array[i][len(array)-1] == 1:
#         count += 1
#
# print(count)

# 반대로 0을 넣고 1의 둘레를 찾아도 되지만, 0의 위치에서 찾기 어렵다



# 색종이 배치

type = 0
# paper = []
#
# paper = [[2, 3, 4, 4], [6, 7, 4, 4]]
# print((paper[0][2]*paper[0][3])+(paper[1][2]*paper[1][3]))

# for i in range(2):
#     paper.append(list(map(int, input().split())))

r, c, w, h = map(int, input().split())

array = [[0 for _ in range(100)] for _ in range(100)]

for i in range(r-1, r+w+1):
    for j in range(c-1, c+h+1):
        if i == r-1 or i == r+w or j == c-1 or j == c+h:
            array[i][j] = 2
        else:
            array[i][j] = 1

r, c, w, h = map(int, input().split())

count_2 = 0
count_1 = 0

for i in range(r, r+w+1):
    for j in range(c, c+h+1):
        if array[i][j] == 2:
            count_2 += 1
        elif array[i][j] == 1:
            count_1 += 1

if count_2 >= 2 and count_1 == 0:
    type = 2
elif count_2 == 1 and count_1 == 0:
    type = 1
elif count_1 >= 1:
    type = 3
else:
    type = 4

print(type)
