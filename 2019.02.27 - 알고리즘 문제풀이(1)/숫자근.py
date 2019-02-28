import sys
sys.stdin = open("숫자근_input.txt")


def root_calc(num):  # 숫자근 구하는 함수

    while True:  # 숫자근이 한 자리가 되면 끝남
        tot = 0
        while num:  # 이 부분은 리스트를 이용해 각 자리를 더하는 방식으로 풀어도 무방
            tot += num % 10
            num //= 10

        if tot < 10: return tot
        num = tot


N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

root_max = 0   # 최대 숫자근
sol = 0   # 그 때의 정수

for i in range(N):
    root = root_calc(arr[i])
    # 숫자근 함수 - 가장 큰 숫자근이면 해당 정수를 solution 변수에, 가장 큰 숫자근과 같다면 더 작은 정수를 솔루션으로 이동

    # 가장 큰 숫자근이면 해당 정수를 solution에 넣기
    if root_max < root:
        root_max = root
        sol = arr[i]

    # 가장 큰 숫자근과 같으면 더 작은 정수를 solution으로
    if root_max == root:
        if sol > arr[i]:
            sol = arr[i]

print(sol)