import sys
sys.stdin = open("토너먼트 카드게임_input.txt")

def tournament(card):

    i = 2

    A = card[0:int((i+j)//2)]
    B = card[int(((i+j)//2)+1):len(card)]


    # for i in range(0, len(card), 2):
    #     if (card[i] == 1 and card[i+1] == 2) or (card[i] == 2 and card[i+1] == 3) or (card[i] == 3 and card[i+1] == 1):
    #         win[i+1] = 1
    #     elif (card[i] == 2 and card[i+1] == 1) or (card[i] == 3 and card[i+1] == 2) or (card[i] == 1 and card[i+1] == 3):
    #         win[i] = 1
    #     else:
    #         win[i] = 1
    #
    # if sum(win) == 1:
    #     for i in range(len(card)):
    #         if win[i] == 1:
    #             return i
    # else:
    #     for i in range(len(card)):
    #         if win[i] == 1:
    #             card2.append(card[i])
    #     tournament(card2)



T = int(input())

for tc in range(T):

    N = int(input())
    card = list(map(int, input().split()))

    print(f'#{tc+1} {tournament(card)}')
