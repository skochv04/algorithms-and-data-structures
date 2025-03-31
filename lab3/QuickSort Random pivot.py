import random
def quick_sort(A, p, r):
    if p < r:
        rand = random.randint(p, r - 1)
        A[rand], A[r] = A[r], A[rand]
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


T = [10, 1, 2, 9, 6, 3, 4, 5, 6, 77, 11]
quick_sort(T, 0, len(T)-1)
print (T)