def findmax(T):
    n = len (T)
    max_el = 0
    for i in range (n):
        if T[i] > max_el:
            max_el = T[i]
    return max_el

def count_sort_moj(T):
    n = len(T)
    c = [0 for _ in range(findmax(T) + 1)]
    output = [0 for _ in range(n)]
    for i in range(n):
        c[T[i]] += 1
    for i in range(1, len(c)):
        c[i] += c[i - 1]
    for i in range(n):
        c[T[i]] -= 1
        output[c[T[i]]] = T[i]
    for i in range(n):
        T[i] = output[i]
    return T

def counting_sort(A, k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1): #zachowujemy stabilność!!!
        C[A[i]]-=1
        B[C[A[i]]] = A[i]
    for i in range(n):
        A[i] = B[i]
    return B

T = [96, 11, 17, 7, 34, 45]
print (counting_sort(T, 100))