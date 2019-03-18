import sys
sys.stdin = open("input_input.txt")

N = int(input())
A, B = list(map(int, input().split()))
cmd = [list(map(int, input())) for _ in range(A)]

# for i in range(A):
#     cmd.append(list(map(int, input())))

print(N)
print(A, B)
for i in range(A):
    for j in range(B):
        print(cmd[i][j], end="")
    print()

