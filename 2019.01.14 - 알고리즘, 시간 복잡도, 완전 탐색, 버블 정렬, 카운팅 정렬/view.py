import sys

sys.stdin = open("view_input.txt")     # 표준 입력 - 제출시에는 주석처리

T = 10   # test case

for tc in range(T):
    count = 0   # 정답의 개수
    N = int(input())   # 각 테스트셋의 건물 개수
    data = list(map(int, input().split()))   # 한 줄을 문자열로 받음 -> 숫자로 바꾸고 공백으로 쪼개서 리스트에 넣음
    print(N, data)


#   K, P = map(int, input().split())  # 만약 2개를 받는 경우

    for i in range(2, len(data)-2):
        if data[i] > data[i+1] and data[i] > data[i+2] and data[i] > data[i-1] and data[i] > data[i-2]:
            count += min(data[i]-data[i-1], data[i]-data[i-2], data[i]-data[i+1], data[i]-data[i+2])

    print("#{} {}".format(tc+1, count))



