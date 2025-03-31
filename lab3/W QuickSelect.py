def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i + 1

def quick_select(T, k, p, r):
    q = partition(T, p, r)
    if q == k:
        return T[q]
    if q < k:
        return quick_select(T, k, q + 1, r)
    else:
        return quick_select(T, k, p, q - 1)

T = [51, 56, 45, 6, 75, 52, 49, 58, 71, 36]
# T = [56, 45, 6, 75, 52]
n = len(T)
print(quick_select(T, 3, 2, 5))

























