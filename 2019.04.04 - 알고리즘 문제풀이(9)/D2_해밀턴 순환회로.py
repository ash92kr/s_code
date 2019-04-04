import sys
sys.stdin = open("D2_해밀턴 순환회로_input.txt")

def DFS(city, count, cost):   # 도시, 순회횟수, 비용

    global min_fee

    if cost > min_fee:  # 가지치기
        return

    # 마지막에 지나치기 이전에 count와 비교해야 한다
    if count == N:   # 순회 횟수가 N번이면 마무리
        if fare[city][0] != 0:  # 집으로 가는 비용이 있어야 한다
            if min_fee > cost + fare[city][0]:   # 행은 현재 있는 곳
                min_fee = cost + fare[city][0]   # 0번 열이 집으로 가는 길
        return
    
    # visited 탐색 범위 : 2~N번 까지만 탐색
    # 방문하는 비용이 있고, 방문하지 않은 도시 찾기
    # 돌아나갈 때, visited 풀어야 한다
    # 집으로 가는 비용이 없는 경우 문제가 되므로 비용이 있는지 체크하기

    # 현재 도시에서 비용이 있고 방문안한 도시를 모두 시도
    for i in range(1, N):
        if fare[city][i] != 0 and visited[i] == 0:
            visited[i] = 1
            DFS(i, count+1, cost+fare[city][i])
            visited[i] = 0


# 현재 위치에서 다음 위치로 어디를 가야 하는가?

N = int(input())

fare = [list(map(int, input().split())) for _ in range(N)]

# print(fare)

visited = [0] * N

min_fee = 987654321

DFS(0, 1, 0)  # 내가 방문하려는 도시 = depth, 순회횟수 1회, 비용 0원

print(min_fee)
