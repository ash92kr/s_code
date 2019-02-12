def fibo1(n):
    global memory
    if n >= 2 and len(memo) <= n:   #
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]
print(fibo1(20))