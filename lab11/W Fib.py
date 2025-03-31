def fib_rek(n):
    if n < 2:
        return 1
    return fib_rek(n-1) + fib_rek(n-2)

def fib_dyn(n):
    F = [1] * (n+1)
    for i in range(2, n + 1):
        F[i] = F[i-1] + F[i-2]
    return F[n]

print (fib_rek(24), fib_dyn(24))