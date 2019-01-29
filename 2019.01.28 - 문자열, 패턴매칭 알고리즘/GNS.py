import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input())

for testcase in range(T):
    temp = input()  # #1 7041을 dummy로 처리(len 함수 이용)
    data = list(map(str, input().split()))

    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    repeat = []

    for i in range(len(num)):
        repeat.append(data.count(num[i]))   # num 리스트에 있는 표현이 data에 몇 번 있는지 count 함수를 사용한 값을 repeat 리스트에 넣음

    print(f'#{testcase + 1}')   # #1 출력용 문구
    for j in range(len(repeat)):   # repeat 리스트에는 모두 10개의 원소가 존재
        # if repeat[j] > 0:
        for k in range(repeat[j]):   # repeat의 해당 원소의 숫자만큼 ZRO 등을 반복해서 출력
            print(num[j], end=" ")
    print()



