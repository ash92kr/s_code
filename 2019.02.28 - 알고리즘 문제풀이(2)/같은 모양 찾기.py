M = int(input())

arr = []

for i in range(M):
    arr.append(list(map(int, input())))

P = int(input())

pattern = []

for i in range(P):
    pattern.append(list(map(int, input())))

# M = 10
#
# P = 3
#
# arr = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
#
# pattern = [[1, 0, 0], [1, 1, 1], [1, 0, 0]]



answer = 0

for i in range(M-P+1):   # 모눈종이의 시작행 제어
    for j in range(M-P+1):   # 모눈종이의 시작열 제어
        flag = 0
        count = 0
        for k in range(P):   # 패턴행
            for l in range(P):   # 패턴열
                if arr[i+k][j+l] == pattern[k][l]:
                    count += 1
                else:
                    flag = 1
                    break
            if flag == 1:  # flag가 1이면 불일치
                break
        if count == (P*P):   # 모든 패턴 매치가 일치해야 한다
            answer += 1

print(answer)










