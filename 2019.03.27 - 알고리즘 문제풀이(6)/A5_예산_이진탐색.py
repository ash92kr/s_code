import sys
sys.stdin = open("예산_input.txt")

# 상한액으로 지방에서 요청액을 배정가능하면 배정하고 아니면 상한액으로 합계 계산
# 합계가 총액 이하면 성공, 아니면 실패 리턴

def check(mid):

    global M

    temp = 0

    for i in range(N):
        if data[i] < mid:
            temp += data[i]
        else:
            temp += mid

    if temp <= M:
        return True
    else:
        return False


N = int(input())
data = list(map(int, input().split()))
M = int(input())

start = min(data)  # 초기값 배정
end = max(data)   # 상한액 배정
money = 0

# 1원부터 max원까지 상한가를 mid로 결정해 총액이하면 상한액을 늘리고 아니면 줄임
while start <= end:
    mid = (start + end)//2
    if check(mid):   # 성공하면 상한액을 늘림
        start += 1
        money = mid   # mid값 백업
    else:  # 초과하면 상한액을 줄임
        end -= 1

print(money)



