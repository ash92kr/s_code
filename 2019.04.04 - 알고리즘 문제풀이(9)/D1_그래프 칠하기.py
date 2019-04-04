# 연결된 상태를 보면서 따라가는 방식이 그래프의 위주
# 1번 노드부터 칠하므로 depth는 N+1이 된다 - 색상 번호도 낮은 숫자부터 실시

import sys
sys.stdin = open("D1_그래프 칠하기_input.txt")


def check(node, color):

    # 현재 노드와 연결된 노드와 중복색상 여부 체크
    for i in range(node):   # 현재 노드 이전까지만 확인하면 된다(열 번호)
        if arr[node][i] == 1 and record[i] == color:  # 현재 노드와 연결되고, 인접노드의 색상이 칠하려는 색상과 같다면 false
            return False

    return True   # 가장 마지막까지 갔을 때 True이다

def DFS(node):

    global flag, record

    if node >= N:  # 깊이의 끝까지 오면 성공
        flag = 1
        return  # 여기서 return하면 DFS[node+1]로 이동한다

    # 현재 노드에게 1~M색상을 칠해보는 경우의 수
    for i in range(1, M+1):
    # 현 노드에 칠할 수 있으면 기록하고 다음 노드로
        if check(node, i):
            record[node] = i  # 색상 기록
            DFS(node+1)
        # 돌아와도 덮어씌우면 되므로 상관 없음
            if flag:
                return

N, M = map(int, input().split())   # N = 노드 수, M = 방향 수

# 인접행렬의 반만 알려주는 이유 - 1번 노드부터 칠해야 하기 때문
# 뒤의 노드를 칠할 수 없으면 앞으로 돌아가야 한다
# 행이 현재 노드, 열이 나와 연결된 노드라는 의미
arr = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     print(arr)

record = [0] * N   # 노드에 칠한 색깔을 기록하는 배열
# 나와 연결된 노드이면 다른 색을 칠해야 한다
# 각 노드는 1번 색부터 시작하되, 연결된 노드들의 색상을 보고 색깔 번호를 높인다
# 한 번 칠할 수 있는 색상을 사용하면 바로 flag를 통해 나갈 것

# depth는 노드, 나와 연결된 노드에 칠할 권리를 부여

flag = 0
DFS(0)  # 첫 번째 노드부터 시작

if flag:
    for i in range(N):
        print(record[i], end=" ")
else:
    print('-1')

