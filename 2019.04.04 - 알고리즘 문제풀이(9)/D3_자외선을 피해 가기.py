import sys
sys.stdin = open("D3_자외선을 피해 가기_input.txt")

# 이 문제도 그래프 문제
# map이 너무 커서 BFS를 실시한다 -> 방문한 곳은 또 방문하지 않을 것인가?
# visited을 사용하되, 기록해놓고 지나가자 -> 비교가 가능해 같은 자리를 여러 번 방문 가능 + 최소값일 때만 넣기
# 가지치기 기능 -> 대각선이므로 오른쪽/아래쪽부터 실시하는 것이 더 빠르다(0이 있어 4방향 탐색은 필수)
# 현재 경로의 해와 가볼 위치에 있는 이전 해를 비교
# visited의 초기값으로는 무한대에 가까운 큰 값을 넣는다
# 이전 값보다 작으면 새로운 값을 넣는다 -> 큐가 비었다면 더 이상 갈 곳이 없다
# 최단거리 문제는 DFS가 적합하다

def BFS(x, y):

    queue = []
    queue.append((x, y))  # 1 시작점 큐에 저장(기록)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = 0

    while queue:

        x, y = queue.pop(0)   # 2 큐에서 데이터 읽기

        for i in range(4):

            new_x = x + dx[i]
            new_y = y + dy[i]

            # 3 연결점 찾아 큐에 저장(기록)
            if 0 <= new_x < N and 0 <= new_y < N:
                if visited[new_x][new_y] > visited[x][y] + place[new_x][new_y]:
                    visited[new_x][new_y] = visited[x][y] + place[new_x][new_y]
                    queue.append((new_x, new_y))


N = int(input())

place = [list(map(int, input())) for _ in range(N)]

visited = [[987654321 for _ in range(N)] for _ in range(N)]

min_sum = 0

BFS(0, 0)  # 출발점부터 시작

print(visited[N-1][N-1])  # 4 큐가 빈 상태