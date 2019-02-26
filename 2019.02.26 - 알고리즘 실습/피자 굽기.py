import sys
sys.stdin = open("피자 굽기_input.txt")

T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    cheese = list(map(int, input().split()))

    queue = []

    for i in range(N):
        queue.append([i, cheese[i]])   # 큐에 피자 번호와 치즈 양 리스트로 넣기

    c_max = 0  # 각 큐에서 피자 번호의 최대값을 구할 변수(초기화 위치 주의)

    while True:

        for j in range(len(queue)):  # 현재 큐에서 최대 피자 번호 구하기
            if queue[j][0] > c_max:
                c_max = queue[j][0]

        a = queue.pop(0)   # 큐에서 가장 앞에 있는 피자 꺼내 치즈 양 확인

        if a[1] != 0:   # 치즈가 0이 아니면(남았으면)
            a[1] = a[1] // 2   # 2로 나누어 몫만 취한 다음
            queue.append(a)   # 다시 넣는다(자동으로 마지막으로 이동)
        else:   # 치즈가 0이면 빼낸 다음,
            if c_max + 1 < M:   # 피자 번호가 M일 때까지
                queue.insert(0, [c_max + 1, cheese[c_max+1]])   # 방금 피자를 뺀 위치에 새로운 피자를 넣는다

        if len(queue) == 1:   # 큐의 길이가 하나면 끝냄
            break

    print(f'#{tc+1} {queue[0][0]+1}')

