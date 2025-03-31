# Najdłuzszy wspolny podciag
# 2, 3, 5, 7, 11, 17
# 2, 5, 11, 15, 3, 19
#
# 2 wym tablica, prawy dolny rog

# mamy 2 tablice A i B liczb naturalnych, sa rownej dlugosci
# znajdz najdluzszy wspolny podciag taki sam w dwóch tablicach
# zlozonosc o(n^2)
# najdluzszy wspolny podciag przy zalozeniu, ze i to liczba elementow z A oraz j to liczba elementow z B

def longest_twice(A, B, i, j, lookup):
    if i == 0 or j == 0:
        return 0
    if lookup[i][j] == 0:
        if A[i-1] == B[j-1]:
            lookup[i][j] = longest_twice(A, B, i-1, j-1, lookup) + 1
        else:
            lookup[i][j] = max(longest_twice(A, B, i, j-1, lookup), longest_twice(A, B, i-1, j, lookup))
    return lookup[i][j]

def longest_twice_bootom_up(A, B):
    i = len(A)
    j = len(B)
    T=[[0 for _ in range(i + 1)] for _ in range(j + 1)]
    for a in range(1, i + 1):
        for b in range(1, j + 1):
            if A[a-1] == B[b-1]:
                T[a][b] = T[a-1][b-1] + 1
            else:
                T[a][b] = max(T[a-1][b], T[a][b - 1])
    return T[i][j]


def print_longest(A, B, i, j, lookup):
    if i == 0 or j == 0:
        return []
    if A[i-1] == B[j-1]:
        return print_longest(A, B, i-1, j-1, lookup) + [A[i-1]]
    if lookup[i-1][j] > lookup[i][j-1]:
        return print_longest(A, B, i-1, j, lookup)
    else:
        return print_longest(A, B, i, j-1, lookup)


A = [2, 3, 5, 7, 11, 17]
B = [2, 5, 11, 15, 3, 19]
i = len(A)
j = len(B)
lookup = [[0 for _ in range(i+1)] for _ in range(j+1)]
print(longest_twice(A, B, i, j, lookup))
print(longest_twice_bootom_up(A, B))
print(print_longest(A, B, i, j, lookup))