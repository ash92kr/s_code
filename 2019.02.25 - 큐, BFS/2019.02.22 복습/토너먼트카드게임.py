
def find(l, r):   # 각 집단을 계속해서 반으로 나눔
    if l==r:   # 왼쪽과 오른쪽이 같으면 1개만 남았다는 뜻
        return l
    else:
        r1 = find(l, (l+r)//2)   # l과 r이 다르면 r1과 r2로 계속 쪼개서 위로 올릴 것
        r2 = find((l+r)//2+1, r)
        if card[r1]==card[r2]:   # 1명의 카드를 위로 올려주어야 한다
            return r1    # 카드가 같으면 왼쪽 사람을 위로 올린다
        else:
            if card[r1]==1 and card[r2]==2:             # 가위 vs 바위
                return r2
            elif card[r1]==1 and card[r2]==3:           # 가위 vs 보
                return r1
            elif card[r1]==2 and card[r2]==1:           # 바위 vs 가위
                return r1
            elif card[r1]==2 and card[r2]==3:           # 바위 vs 보
                return r2
            elif card[r1]==3 and card[r2]==1:           # 보 vs 가위
                return r2
            elif card[r1]==3 and card[r2]==2:           # 보 vs 바위
                return r1

# 순서 : find(1, 4) -> find(1, 2) -> find(1, 1)
# find(1, 2) -> r1=1, r2=2(인덱스가 넘어감) -> card[1] > card[3] = 1
# 우측으로 넘어가서 find(3, 4) -> find(4, 4)인데 취소 : r1=3, r2=4 -> card[2] > card[1] = 2

import sys
sys.stdin = open('토너먼트카드게임_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = [0] + list(map(int, input().split()))   # 인덱스 1번부터 저장(시작점이 1)
    print('#{} {}'.format(tc, find(1, N)))
