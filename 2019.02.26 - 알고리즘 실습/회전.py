import sys
sys.stdin = open('회전_input.txt')

T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    queue = list(map(int, input().split()))   # 큐에 넣을 숫자값 받기

    for i in range(M):   # M번 반복
        a = queue.pop(0)   # 첫 번째 원소를 빼내서 가장 마지막에 넣기
        queue.append(a)

    print(f'#{tc+1} {queue[0]}')   # 첫 번째 원소 출력

