import sys
sys.stdin = open("A3_숫자 카운팅_input.txt")

def uppersearch(start, end, data):

    count = -1

    while start <= end:
        mid = (start + end)//2
        if num[mid] < data:   # data보다 작으면 오른쪽 영역 재탐색
            count = mid
            start = mid + 1
        else:   # data보다 크거나 같으면 왼쪽 영역 재탐색
            end = mid - 1

    return count   # 찾지 못하면 -1을 반환할 것


N = int(input())
num = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

for i in range(M):
    print(uppersearch(0, N-1, find[i]+1) - uppersearch(0, N-1, find[i]))

