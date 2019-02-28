import sys
sys.stdin = open("마을 위성사진_input.txt")

N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int, input())))

for h in range(N):  # 시작점 언덕은 1 -> 없을 수도 있다
    flag = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            # 사방이 모두 언덕이면 높이 1 증가
            if arr[i][j] > h:  # 현재 높여주려는 언덕의 높이와 일치하는가?
                flag = 1  # 그런 언덕이 없으면 더 이상 높일 언덕이 없다
                # 현재 높이보다 주변에 있는 언덕들의 높이가 높으면 기준점을 1 높임
                if arr[i-1][j]>h and arr[i][j-1]>h and arr[i+1][j]>h and arr[i][j+1]>h:
                    arr[i][j] += 1
    # 더 이상 높일 언덕이 없으면 탈출
    if flag == 0:
        break

print(h)



