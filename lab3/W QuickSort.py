def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

#usuniecie rekurencji ogonowej
def quicksort_plus(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        p = q + 1
    return A

def partition(A, p, r):
    #Partition Lomuto
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

T = [12, 6, 13, 44, 8, 7, 1]

print(quicksort_plus(T, 0, len(T)-1))








