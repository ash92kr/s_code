import sys
sys.stdin = open("C6_도자기_input.txt")

def DFS(start, count):

    global doja

    if count == M:
        doja += 1
        # for i in range(M):
        #     print(record[i], end=" ")
        # print()
        return

    # backup = 0  # 함수의 지역변수(함수가 호출될 때마다 초기화됨)

    for i in range(start, N):   # 흙의 재료

        # if backup == soil[i]:
        #     continue
        # backup = soil[i]   # 지역변수이므로 초기화를 할 필요가 없다

        if record[count] == soil[i]:   # 이미 담긴 흙과 지금 넣으려는 흙이 같다면 pass
            continue
        record[count] = soil[i]
        DFS(i+1, count+1)   # i+1번째부터 시작
    record[count] = 0   # 지워주기(1번째에 대한 모든 경우의 수를 마친 다음에 지워주어야 한다)


# 우선은 sorting부터 실시해 처음부터 끝까지 돌려보자
# 같은 값을 가진 원소끼리 저장해 중복값은 제외한다
# 그러나 기록을 하게 되면 잔상이 남으므로 돌아올 때 기록한 내용을 지워야 한다
# 리스트에 만들어서 넣고 바로 빼낼 것

# 내가 담았던 것을 기록하기 위해 리스트가 아니라 임시변수 하나만 있어도 된다

# 또는 재료별 개수를 카운팅한다 -> 그 중의 M개를 가지고 서로 다른 경우를 구현한다
# 각 방에 있는 개수의 경우를 가지고 구현한다 -> 조합의 개념으로 구현한다(0개 ~ j개만큼 실시)
# 데이터 편집의 필요성

T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    soil = list(map(int, input().split()))

    soil.sort()   # sorting하는 전제조건 필요

    record = [0] * N

    doja = 0

    DFS(0, 0)   # 0번 요소부터 시작, 개수는 0개

    print(doja)

