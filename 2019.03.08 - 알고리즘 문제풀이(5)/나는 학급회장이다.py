import sys
sys.stdin = open("나는 학급회장이다_input.txt")

N = int(input())

vote = [[0 for _ in range(5)] for _ in range(3)]
# 행(바깥쪽 리스트)을 후보자, 열을 1~3점수대, 4열은 합계(1열은 0번후보이므로 비워둠)

for i in range(N):
    jumsu = list(map(int, input().split()))
    for j in range(3):
        vote[j][jumsu[j]] += 1   # 1번째로 나온 번호가 1번 후보의 점수

for i in range(3):
    vote[i][4] = (vote[i][1] * 1) + (vote[i][2] * 2) + (vote[i][3] * 3)

max_score = vote[0][4]  # 1번 후보를 max로 잡는 것이 유리함
three = vote[0][3]   # arr[max_score]로 가지고 다니면 더욱 짧게 작성 가능
two = vote[0][2]
candidate = 1

for i in range(1, 3):
    if vote[i][4] > max_score:
        max_score = vote[i][4]
        three = vote[i][3]
        two = vote[i][2]
        candidate = i+1
    elif vote[i][4] == max_score:
        if vote[i][3] > three:
            three = vote[i][3]  # 후보자를 바꾸면 최대값도 바꿔야 한다
            candidate = i+1
        elif vote[i][3] == three:
            if vote[i][2] > two:
                two = vote[i][2]
                candidate = i+1
            elif vote[i][2] == two:
                candidate = 0

print(vote)
print("{} {}".format(candidate+1, max_score))
