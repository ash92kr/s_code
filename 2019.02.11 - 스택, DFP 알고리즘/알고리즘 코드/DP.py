def fibo2(n):
    f = [0, 1]

    for i in range(2, n+1):    # 2부터 n까지 반복하면서 (n-1)+(n-2)를 매번 계산한다
        f.append(f[i-1] + f[i-2])

    return f[n]

# 재귀함수 없이 점화식을 표현한 것
# f(n) = f(n-1) + f(n-2)   ==   점화식이 되므로 재귀를 잘 해야 한다

print(fibo2(5000))