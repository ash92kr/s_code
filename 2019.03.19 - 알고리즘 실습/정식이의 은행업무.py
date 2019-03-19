import sys
sys.stdin = open("정식이의 은행업무_input.txt")

T = int(input())

for tc in range(T):

    two = input()
    three = input()

    idx2 = 0   # 이진수의 인덱스

    while idx2 < len(two):   # 2진수 자리 변경

        # 2진수 관련 변수
        flag2 = 0
        temp2 = ""   # index 변경 시마다 초기화 필요
        two_num = 0  # 2진수를 10진수로 변경

        if two[idx2] == '0':   # 문자열은 immutable이므로 다른 문자열에 저장해야 한다
            temp2 = two[:idx2] + '1' + two[idx2+1:]
        else:
            temp2 = two[:idx2] + '0' + two[idx2+1:]

        for i in temp2:
            two_num = (two_num * 2) + int(i)

        # 3진수 관련 변수
        idx3 = 0
        flag3 = 0

        while idx3 < len(three):   # 3진수 자리 변경

            three_num = 0   # 3진수를 10진수로 변경

            temp3 = ""  # 매번 번경시마다 초기화 필요
            temp3 = three[:idx3] + str(flag3) + three[idx3+1:]  # 마찬가지로 3진수를 다른 문자열에 저장함

            for j in temp3:
                three_num = (three_num * 3) + int(j)

            if two_num == three_num:  # 매번 변경할 때 마다 값이 같은지 확인 필요
                print("#{} {}".format(tc+1, two_num))
                flag2 = 1   # 전체 바깥으로 빠져 나가기 위한 변수
                break
            else:
                if flag3 == 2:
                    idx3 += 1
                    flag3 = 0
                else:
                    flag3 += 1

        if flag2 == 1:
            break
        else:
            idx2 += 1

