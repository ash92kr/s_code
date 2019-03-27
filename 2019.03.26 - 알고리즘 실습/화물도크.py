import sys
sys.stdin = open("화물도크_input.txt")


def bubble(time):

    for i in range(N-1):
        for j in range(i+1, N):
            if time[i][1] > time[j][1]:  # 끝 숫자를 기준으로 정렬한다
                time[i], time[j] = time[j], time[i]
            elif time[i][0] == time[j][0]:
                if time[i][1] > time[j][1]:  # 끝 숫자가 같으면 큰 숫자부터 정렬
                    time[i], time[j] = time[j], time[i]


T = int(input())

for tc in range(T):

    N = int(input())

    time = []

    for i in range(N):
        time.append(list(map(int, input().split())))

    bubble(time)

    dok = 0   # max_task
    start = 0

    print(time)

    for j in range(N):   # 시작점을 구한다
        end = 0
        temp = 0
        if start <= time[j][0]:   # 앞에서 부터 start보다 크거나 같으면 변경
            end = time[j][1]   # 끝 값
            temp += 1
            for k in range(j+1, N):  # 끝 값보다 앞 값이 크면 이어짐
                if end <= time[k][0]:
                    end = time[k][1]
                    temp += 1

        if temp > dok:  # 최대 화물차 대수 구하기
            dok = temp

    print("#{} {}".format(tc+1, dok))
