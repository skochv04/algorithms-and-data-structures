# We are given a set of open intervals. Find a subset of this set such that:
#   1) its size is exactly k,
#   2) intervals are disjoint,
#   3) the difference between the earliest start and farthest end is minimal.
# If there is no solution, the algorithm should say no.

def open_intervals(T, k):
    T.sort(key=lambda x: x[1])
    n = len(T)
    print(T)
    best_result = float('inf')
    result = []
    if k < n:
        for i in range(n - k):
            act = T[i]
            s = 1
            tab = [act]
            j = i + 1
            while s < k and j < n:
                if T[j][0] > act[1]:
                    act = T[j]
                    s += 1
                    tab.append(act)
                j += 1
            if s == k:
                dist = tab[-1][1] - tab[0][0]
                if dist < best_result:
                    best_result = dist
                    result = tab[:]
    return result

T = [(1, 7), (2, 5), (3, 4), (9, 10), (3, 6), (2, 4), (5, 9), (7, 8), (1, 5), (1, 2), (2, 5)]
print(open_intervals(T, 3))