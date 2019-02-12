def factorial(n):
    if n == 1:   # 지역변수
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


def fibo(n):
    if n in [1, 2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10))




