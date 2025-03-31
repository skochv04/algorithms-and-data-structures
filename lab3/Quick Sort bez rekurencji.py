def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i + 1

def quicksort (tab):
    stack = []
    stack.append(0, len(tab)-1)
    while len(stack)>0:
        left, right = stack.pop()
        if right-left > 0:
            pivot = partition(tab, left, right)
            stack.append((left, pivot - 1))
            stack.append ((pivot + 1, right))
