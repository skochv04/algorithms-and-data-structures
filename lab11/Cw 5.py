# cw. 4
# mamy ciag macierzy, znamy ich rozmiary, szukamy kolejnosci w jakiej mamy pomnozyc macierze tak by liczba operacji
# podczas mnozenia macierzy byla jak najmniejsza, innymi slowy jak najmniejszy koszt

inf = float('inf')

def matrixChainMultiplication(T, i, j):
    if j <= i + 1:
        return 0
    res = float('inf')
    for k in range(i + 1, j):
        cost = matrixChainMultiplication(T, i, k)
        cost += matrixChainMultiplication(T, k, j)
        cost += T[i] * T[k] * T[j]
        res = min(res, cost)
    return res

def matrixChainMultiplication_dyn(T, i, j, tab):
    if j <= i + 1:
        return 0, tab
    if tab[i][j] != inf:
        return tab[i][j], tab
    for k in range(i + 1, j):
        cost = matrixChainMultiplication_dyn(T, i, k, tab)[0]
        cost += matrixChainMultiplication_dyn(T, k, j, tab)[0]
        cost += T[i] * T[k] * T[j]
        tab[i][j] = min(tab[i][j], cost)
    return tab[i][j], tab

def matrixChainMultiplication_dyn2(T):
    n = len(T)
    tab = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for length in range(2, n + 1):  # subsequence lengths
        for i in range(1, n - length + 2):
            j = i + length - 1
            tab[i][j] = inf
            if j < n:
                for k in range(i, j):
                    tab[i][j] = min(tab[i][j], tab[i][k] + tab[k + 1][j] + T[i - 1] * T[k] * T[j])
    print(*tab, sep='\n')
    return tab[1][n - 1]

def my_matrixChain(T):
    n = len(T)

    DP = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n - 2):
        j = i + 2
        DP[i][j] = T[i] * T[i + 1] * T[j]
    for k in range(3, n):
        for i in range(n - 3):
            j = i + k
            if j < n:
                DP[i][j] = min(DP[i+1][j] + T[i] * T[i+1] * T[j], DP[i][j - 1] + T[i] * T[j-1] * T[j])
    print(*DP, sep='\n')

T0 = [10, 30, 5, 60]

T = [5, 6, 4, 2, 3]
tab = [[inf for _ in range(len(T))] for _ in range(len(T))]

# print(matrixChainMultiplication(T, 0, len(T) - 1))
# print(*matrixChainMultiplication_dyn(T, 0, len(T) - 1, tab)[1],sep='\n')
# print()
# print(matrixChainMultiplication_dyn2(T))
print(my_matrixChain(T))