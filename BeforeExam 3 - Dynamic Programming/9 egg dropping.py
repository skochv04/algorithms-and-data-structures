# Given number of floors and number of eggs. Find the minimum number of attempts
# (drops) that is required to know the floor from which if the egg is dropped,
# it will break.

inf = float('inf')

def egg_drop(eggs, floors):
    T = [[inf for _ in range(floors + 1)] for _ in range(eggs + 1)]
    for i in range(1, floors + 1):
        T[0][i] = i
        T[1][i] = i
    for i in range(1, eggs + 1):
        T[i][0] = i
        T[i][1] = i
    for i in range(2, eggs + 1):
        for j in range(i, floors + 1):
            for k in range(1, j + 1):
                T[i][j] = min(T[i][j], 1 + max(T[i-1][k-1], T[i][j-k]))
    return T[-1][-1]

eggs = 2
floors = 24
print(egg_drop(eggs, floors))