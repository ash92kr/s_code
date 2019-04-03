import sys
sys.stdin = open("연산_input.txt")

def BFS(start, end):

    queue = []
    queue.append((start, 0))

    dx = [1, 1, 10, 2]

    visited = [0] * (1000001)
    visited[start] = 1

    temp = 0

    while queue:

        # x, count = queue.pop(0)

        x = queue[temp][0]
        count = queue[temp][1]

        for i in range(4):

            if i == 0:
                new_x = x + dx[i]
            elif i == 1 or i == 2:
                new_x = x - dx[i]
            else:
                new_x = x * dx[i]

            if new_x < 1 or new_x >= 1000001:
                continue
            if visited[new_x] == 1:
                continue
            if new_x == end:
                return count + 1

            queue.append((new_x, count+1))
            visited[new_x] = 1

        temp += 1  # 모든 반복문을 마친 다음에 돈다

    return -1


T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    print("#{} {}".format(tc+1, BFS(N, M)))
