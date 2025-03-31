# Vasya takes part in the orienteering competition. There are n checkpoints located along the
# line at coordinates x[1], x[2], ..., x[n]. Vasya starts at the point with coordinate a. His
# goal is to visit at least n-1 checkpoint in order to finish the competition. Participant
# are allowed to visit checkpoints in arbitrary order. Vasya wants to pick such checkpoints and
# the order of visiting them that the total distance travelled is minimized. He asks you to
# calculate this minimum possible value.

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(T, i, n):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and T[l] > T[max_ind]:
        max_ind = l
    if r < n and T[r] > T[max_ind]:
        max_ind = r
    if max_ind != i:
        T[i], T[max_ind] = T[max_ind], T[i]
        heapify(T, max_ind, n)

def heap_build(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, i, n)

def heap_sort(T):
    n = len(T)
    heap_build(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, 0, i)

def checkpoints(n, a, T):
    if n == 1:
        return 0
    heap_sort(T)
    n = len(T)
    d1 = T[n-1] - T[1]
    d2 = T[n-2] - T[0]
    d_to1 = abs(a - T[1])
    d_to2 = abs(a - T[0])
    d_ton1 = abs(a - T[n-1])
    d_ton2 = abs(a - T[n-2])
    return min(d_to1 + d1, d_to2 + d2, d_ton1 + d1, d_ton2 + d2)

n = 9
a = -3
T = [-10, -7, -3, -4, 7, -6, 10, -10, -7]
print(checkpoints(n, a, T))