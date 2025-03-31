#QS, ale max O(log n) pamięci

def partition (T, p, r):
    if (p >= r):
        return p
    pivot = T[r]
    j = p
    for i in range (p, r, 1):
        if (T[i] < pivot):
            T[i], T[j] = T[j], T[i]
            j += 1
    T[r], T[j] = T[j], T[r]
    return j

def quicksort (T, p, r):
    while (p < r):
        pivot = partition(T, p, r)
        if (r - pivot > pivot - p):
            quicksort(T, p, pivot - 1)
            p = pivot + 1
        else:
            quicksort(T, pivot - 1, r) #може плюс?
            r = pivot - 1