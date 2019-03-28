import sys
sys.stdin = open("숫자 찾기(이진탐색)_input.txt")

def find_num(start, end, data):

    while start <= end:
        mid = (start + end) // 2
        if data == num[mid]:   # num의 중간값과 data가 같으면 인덱스 + 1
            return mid + 1
        elif data > num[mid]:   # data가 num보다 크면 보다 작은쪽을 탐색
            start = mid + 1
        else:
            end = mid - 1    # data가 num보다 작으면 보다 큰쪽을 탐색

    return 0  # 아무 것도 없는 경우


N = int(input())
num = list(map(int, input().split()))
T = int(input())
find = list(map(int, input().split()))

for i in range(T):   # T를 통해서 값을 넘겨줌
    print(find_num(0, N-1, find[i]))  # start와 end는 인덱스 범위이다

