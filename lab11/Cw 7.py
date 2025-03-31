#Zadanie 7
#Шахівниця, кожна клітинка має певну ціну, потрібно дійти до правого нижнього кутка найдешевшим шляхом, можемо йти
#тільки вправо або вниз
#2^N -> N^2
#dekorator cache???

import random
# inf = 10**100
inf = float('inf')

def chessboard(T, w, k):
    if w == 0 and k == 0:
        return 0
    if w < 0 or k < 0:
        return inf
    return T[w][k] + min(chessboard(T, w-1, k), chessboard(T, w, k-1))

def chessboard_dynamik1(T, tab, w, k):
    if w == 0 and k == 0:
        return 0
    if w < 0 or k < 0:
        return inf
    if tab[w][k] == inf:
        tab[w][k] = T[w][k] + min(chessboard_dynamik1(T, tab, w-1, k), chessboard_dynamik1(T, tab, w, k-1))
    return tab[w][k]

def chessboard_dynamik2(T, w, k):
    #bez rekurencji
    n = len(T)
    F = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n+1):
        F[0][i] = inf
        F[i][0] = inf
    for i in range(1, n+1):
        for j in range(1, n+1):
            if not (i == j == 1):
                F[i][j] = T[i-1][j-1] + min(F[i][j-1], F[i-1][j])
    return F[w+1][k+1]

def chessboard_dynamik3(T, w, k):
    #bez rekurencji
    n = len(T)
    F = [[0 for _ in range(n)] for _ in range(n)]
    # F[0][0] = inf
    F[0][1] = T[0][1]
    F[1][0] = T[1][0]
    for i in range(2, n):
        F[0][i] = F[0][i-1] + T[0][i]
        F[i][0] = F[i-1][0] + T[i][0]
    for i in range(1, n):
        for j in range(1, n):
            F[i][j] = T[i][j] + min(F[i][j-1], F[i-1][j])
    return F[w][k]

n = 4
# T = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]
T = [[3, 2, 1, 5],
     [2, 5, 4, 2],
     [1, 2, 5, 5],
     [2, 4, 2, 3]]
print(*T, sep='\n')
tab = [[inf for _ in range(n)] for _ in range(n)]
print(chessboard(T, n-1, n-1))
print(chessboard_dynamik1(T, tab, n-1, n-1))
print(chessboard_dynamik2(T, n-1, n-1))
print(chessboard_dynamik3(T, n-1, n-1))