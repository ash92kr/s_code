def check():

    global flag

    check = 0

    if a[0] == a[1] and a[1] == a[2]:
        check += 1
    if a[3] == a[4] and a[4] == a[5]:
        check += 1
    if a[0]+1 == a[1] and a[1]+1 == a[2]:
        check += 1
    if a[3]+1 == a[4] and a[4]+1 == a[5]:
        check += 1

    if check == 2:
        flag = 1
        return   # 의미 없는 return이다


def perm(n, k):
    if n == k:
        check()
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]


flag = 0
a = [1, 2, 4, 7, 6, 3]
perm(6, 0)

if flag:
    print("BabyGin")
else:
    print("Not BabyGin")





