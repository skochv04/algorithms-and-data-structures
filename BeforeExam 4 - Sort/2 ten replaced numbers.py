# We are given an array with n (n >= 11) natural numbers in the range [0, k]. 10 numbers from this array
# were replaced with random numbers outside this range (e.g. much greater or negative numbers). Find
# algorithm that sorts the array in the O(n) time.

def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        while i > 0 and T[i] < T[i-1]:
            T[i], T[i-1] = T[i-1], T[i]
            i -= 1
    return T

def counting_sort(A, k):
    n = len(A)
    C = [0] * (k+1)
    B = [0] * n
    for i in range(n):
        if 0 <= A[i] <= k:
            C[A[i]] += 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1): #zachowujemy stabilność!!!
        if 0 <= A[i] <= k:
            C[A[i]]-=1
            B[C[A[i]]] = A[i]
    for i in range(n):
        A[i] = B[i]
    return B

def replaced_numbers(T, k):
    n = len(T)
    N = [0 for _ in range(10)]
    j = 0
    for i in range(n):
        if not 0 <= T[i] <= k:
            N[j] = T[i]
            j += 1
    first = counting_sort(T, k)
    second = insertion_sort(N)
    j = 0
    while j < len(second) and second[j] < 0:
        T[j] = second[j]
        j += 1
    i = 0
    m = j
    while i < len(first) and first[i] != 0:
        T[j] = first[i]
        i += 1
        j += 1
    while m < len(second) and second[m] >= k:
        T[j] = second[m]
        j += 1
        m += 1
    return T

T = [1, -100, 2, 3, 32, 6, 7, 7, -203, 8, 9, -42, 14, 15, 57, 16, 67, 18, 46, 19, 65, 19, 20, 91, 134, 21, 25]
k = 25
print(replaced_numbers(T, k))