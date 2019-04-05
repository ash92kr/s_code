import sys
sys.stdin = open('(5248)그룹나누기_input.txt', 'r')
T = int(input())

def findSet(x):   # 최상위 부모의 값이 나온다 -> 자기 자신이 자기를 가리키는 것을 찾으면 된다
    if x == parent[x]: return x
    else: return findSet(parent[x])

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = list(range(N + 1))

    for i in range(M):
        a = arr[2 * i]
        b = arr[2 * i + 1]
        parent[findSet(b)] = findSet(a)  # b의 대표 원소를 a의 대표원소로 교체

    cnt = 0;
    for i in range(1, N + 1):  # 대표원소가 자기 자신인 경우의 수
        if parent[i] == i:   # 이것을 찾으면 된다
            cnt += 1
    print('#{} {}'.format(tc, cnt))
