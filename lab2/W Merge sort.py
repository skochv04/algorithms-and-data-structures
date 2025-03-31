def merge_sort (T):
    n = len(T)
    if n > 1:
        mid = n//2
        left = T[:mid]
        right = T[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                T[k] = left[i]
                i += 1
            else:
                T[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            T[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            T[k] = right[j]
            j += 1
            k += 1



def wypisz(T):
    for i in range(len(T)):
        print(T[i], end=" ")
    print()

T = [38, 27, 43, 3, 9, 82, 10]
wypisz(T)
merge_sort(T)
wypisz(T)