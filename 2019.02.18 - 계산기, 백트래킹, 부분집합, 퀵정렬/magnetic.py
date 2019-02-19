import sys
sys.stdin = open("magnetic_input.txt")

for tc in range(10):

    L = int(input())   # 행 수

    mag = []   # 테이블(100행*100열)

    for i in range(L):
        mag.append(list(map(int, input().split())))   # 데이터 받아오기

    deadlock = 0   # 교착(1-2)인 경우 count할 개수

    for i in range(len(mag[0])):  # 세로로 2차원 리스트 순회
        last = []   # 스택(j = 0인 경우 초기화) -> 1이 남아있는 경우 제거
        for j in range(len(mag)):
            if mag[j][i] == 1 and len(last) == 0:  # 가장 처음에 2가 나오면 제외
                last.append(mag[j][i])
            elif mag[j][i] == 2 and len(last) != 0:   # 1이 들어간 상태로 2가 나오면 pop
                last.pop()
                deadlock += 1   # 교착횟수 추가

    print(f'#{tc+1} {deadlock}')




