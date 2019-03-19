import sys
sys.stdin = open("이진수_input.txt")

T = int(input())

def hex_bin(i):

    mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
               'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    return mapping[i]   # 딕셔너리의 value 출력

for tc in range(T):

    N, hex = map(str, input().split())

    bin = ""   # 2진수 담을 그릇

    for i in hex:
        bin += hex_bin(i)

    print("#{} {}".format(tc+1, bin))


