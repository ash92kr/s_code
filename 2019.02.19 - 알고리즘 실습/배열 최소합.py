import sys
sys.stdin = open("배열 최소합_input.txt")


def make_permutation(visited, k, depth, part):

    global N, data

    in_perm = [False] * len(data)

    for i in range(1, k):
        in_perm[visited[i]] = True

    ncands = 0

    for i in range(1, depth+1):
        if in_perm[i] == False:
            part[ncands] = i
            ncands += 1
    return ncands


def backtrack(visited, k, depth):

    global N, arr, data

    part = [0] * N

    if k == depth:
        for i in range(1, k+1):
            if visited[i]:
                print(arr[visited[i]], end=" ")
        print()
    else:
        k += 1
        ncands = make_permutation(visited, k, depth, part)
        for i in range(ncands):
            visited[k] = part[i]
            backtrack(visited, k, depth)


T = int(input())

for tc in range(T):

    N = int(input())

    arr = []   # 실제 데이터가 들어가는 배열

    for i in range(N):
        # arr.append(list(map(int, input().split())))
        arr += map(int, input().split())

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    visited = [0] * len(data)   # 방문했는지 여부 체크하는 리스트

    print(f'#{tc+1} {backtrack(visited, 0, N)}')














