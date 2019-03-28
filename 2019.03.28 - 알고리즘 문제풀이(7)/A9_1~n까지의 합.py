import sys
sys.stdin = open("A9_1~n까지의 합_input.txt")

def DFS(N):

    hab = N

    if N == 1:
        return 1
    else:
        hab += DFS(N-1)
    return hab


N = int(input())

print(DFS(N))