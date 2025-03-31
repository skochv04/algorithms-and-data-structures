from egz1btesty import runtests
inf = float('inf')

def planets( D, C, T, E ):
    n = len(D)
    DP = [[inf for _ in range(E + 1)] for _ in range(n)]
    DP[0][0] = 0
    for b in range(1, E + 1):
        DP[0][b] = b * C[0]
    if T[0][0] != 0:
        DP[T[0][0]][0] = T[0][1]
    for i in range(1, n):
        dist = D[i] - D[i-1]
        for b in range(E):
            if b + dist < E + 1 and DP[i][b] > DP[i-1][b+dist]:
                DP[i][b] = DP[i-1][b+dist]
        for j in range(1, E + 1):
            if DP[i][j] > DP[i][j-1] + C[i]:
                DP[i][j] = DP[i][j-1] + C[i]
        if i != T[i][0]:
            DP[T[i][0]][0] = min(DP[T[i][0]][0], DP[i][0] + T[i][1])
    # print(*DP, sep='\n')
    return min(DP[n-1])


# D = [ 0, 5, 10, 20]
# C = [ 2, 1, 3, 9]
# T = [(2,3), (3,7), (2,10), (3,10)]
# E = 10

D = [0, 1, 4, 6, 7, 10, 11, 12, 13, 15, 16]
C = [2, 6, 2, 10, 2, 10, 4, 6, 8, 8, 4]
T = [(0, 0), (5, 8), (2, 0), (7, 10), (10, 6), (10, 26), (10, 6), (10, 2), (8, 0), (9, 0), (10, 2)]
E = 5
# Prawidlowy wynik :  20
# Wynik algorytmu  :  24
print(planets(D, C, T, E))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )