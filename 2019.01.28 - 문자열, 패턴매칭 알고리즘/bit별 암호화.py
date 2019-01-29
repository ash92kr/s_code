def Bbit_print(a):
    for i in range(7, -1, -1):
        if a & (1<<i):
            print(1, end="")
        else:
            print(0, end="")
    print()

a = 0x86   # 16진수 86
key = 0xAA   # 16진수 AA
print("a      ==>", end=" ")
Bbit_print(a)   # 평문

print("a^=key ==>", end=" ")
a ^= key
Bbit_print(a)   # XOR을 이용한 암호문(같으면 0, 다르면 1)

print("a^=key ==>", end=" ")
a ^= key
Bbit_print(a)   # 복호문
