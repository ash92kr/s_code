def bit_print(i):
    output = ""
    for j in range(7, -1, -1)   # 모두 8자리
        if i & (1 << j):   # 하나라도 1이 있으면 각 자리에 1을 붙임
            output += "1"
        else:
            output += "0"   # 하나라도 1이 없으면 각 자리에 0을 붙임
    print(output)

for i in range(-5, 6):
    print("%3d = " % i, end="")
    bit_print(i)

