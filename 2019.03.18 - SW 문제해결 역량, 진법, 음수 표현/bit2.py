def bit_print(i):
    output = ""
    for j in range(7, -1, -1):
        if i & (1 << j):
            output += "1"
        else:
            output += "0"
    print(output)

a = 0x86
key = 0xAA

print("a     ==> ", end="")
bit_print(a)

print("a^=   ==> ", end="")
a ^= key
bit_print(a)

print("a^=   ==> ", end="")
a ^= key
bit_print(a)