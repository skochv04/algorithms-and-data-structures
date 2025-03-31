# mamy tablice A liczb naturalnych
# znajdz najdluzszy rosnacy podciag

# f jest zawsze posortowane wiec drugiego fora zastepujemy binsearchem
# i otrzymujemy zlozonosc nlogn

def longest(A):
    n = len(A)

def lis(A):
    n = len(A)
    F = [1] * n
    P = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
    last = -1
    maximum = -1
    for i in range(n):
        if F[i] > maximum:
            last = i
            maximum = F[i]
    return last, maximum, P

def ps(A, P, i):
    if P[i] != -1:
        ps(A, P, P[i])
    print(A[i], end = " ")

A = [17, 48, 1, 2, 3, 4, 3, 38, 7, 8, 9]
print(lis(A))