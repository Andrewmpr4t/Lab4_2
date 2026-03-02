def fibonacci(n):
    if n <= 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fact(n-1)
