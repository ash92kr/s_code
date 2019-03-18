# text = list(map(int, input()))
#
# pattern = list(map(int, input()))

text = "0269FAC9A0"

bit = ""

two = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
       '4': '0100', '5': '0101', '6': '0110', '7': '0111',
       '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
       'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

for i in range(len(text)):
    bit += two[text[i]]

print(bit)

pattern = ['001101', '010011', '111011', '110001', '100011',
           '110111', '001011', '111101', '011001', '101111']

# count = [0] * 10

idx = 0

while idx <= len(bit)-5:
# for i in range(len(bit)-5):
    temp = bit[idx:idx+6]
    flag = 0

    for i in range(len(pattern)):
        if str(temp) == pattern[i]:
            print(i, end=" ")
            flag = 1

    if flag:
        idx += 6
    else:
        idx += 1

# for i in range(10):
#     if count[i] >= 1:
#         print(i, end=", ")

