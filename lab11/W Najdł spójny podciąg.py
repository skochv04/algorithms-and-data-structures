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

A = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]
print(lis(A))
ps(A, lis(A)[2], lis(A)[0])