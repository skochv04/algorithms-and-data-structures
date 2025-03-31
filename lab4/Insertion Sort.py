def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        while i > 0 and T[i] < T[i-1]:
            T[i], T[i-1] = T[i-1], T[i]
            i -= 1

T = [2, 8, 5, 3, 4, 1, 17]
insertion_sort(T)
print(T)