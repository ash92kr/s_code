import sys
sys.stdin = open("덧셈_input.txt")

S, X = map(str, input().split())
flag = 0

for i in range(1, len(S)):
    SA = S[:i]
    SB = S[i:]
    if int(SA) + int(SB) == int(X):
        print("{}+{}={}".format(int(SA), int(SB), int(X)))
        flag = 1

if flag == 0:
    print("NONE")
