from zad8testy import runtests
from collections import deque
inf = float('inf')

#Stas Kochevenko
#Opis: W danym algorytmie najpierw szukamy algorytmem BFS dla każdego pola, po którym może się poruszać Maksymilian, objętość ropy
#ze spójnej składowej z tym polem, więc mamy tablicę jednowymiarową po której on będzie się poruszał. Następnie tworzymy listę, w krótej
#są indeksy niezerowych pól (czyli Maksymilian może potencjalnie się tam zatrzymać). Dalej będziemy wypełniać nową tablicę [new_n] x [count + 1],
#gdzie new_n - to rozmiar listy niezerowych pól, a count - to łączna suma wszystkich objętości rop na mapie. Wypełniając tą tablicę będziemy próbowali
#dotrzeć do każdego następnego pola i z listy niezerowych pól, i jeżeli da się to zrobić w mniej skoków, to będziemy wpisywać ilość kroków dotarcza do pola i + 1.
#W wyniku działania algorytmu zwrócamy minimalną wartóść zatrzymywań z ostatniego wiersza tablicy.

def find_oil(T):
    n = len(T) #wiersz
    m = len(T[0]) #kolumna
    W = [0 for _ in range(m)]
    visited = []

    def BFS(u, v):
        q = deque()
        q.append((u, v))
        visited.append((u, v))
        sum = T[u][v]
        while len(q) != 0:
            a, b = q.popleft()
            for i, j in get_neighbors(a, b):
                if T[i][j] != 0 and (i, j) not in visited:
                    visited.append((i, j))
                    sum += T[i][j]
                    q.append((i, j))
        return sum


    def get_neighbors(u, v):
        neighbors = []
        if u > 0:
            neighbors.append((u - 1, v))
        if u < n - 1:
            neighbors.append((u + 1, v))
        if v > 0:
            neighbors.append((u, v - 1))
        if v < m - 1:
            neighbors.append((u, v + 1))
        return neighbors

    for j in range(m):
        if T[0][j] != 0:
            W[j] = BFS(0, j)

    return W

def my_zaba(T):
    n = len(T)
    energy = sum(T) + 1
    dp = [[(inf, 0) for _ in range(energy + 1)] for _ in range(n)]
    dp[0][T[0]] = (0, 1)
    for i in range(1, n):
        for j in range(energy):
            if dp[i-1][j+1][0] < dp[i][j][0]:
                dp[i][j] = (dp[i-1][j+1][0] + dp[i-1][j+1][1], 0)
                if dp[i][j][0] < dp[i][j + T[i]][0]:
                    dp[i][j + T[i]] = (dp[i][j][0], 1)
    return min(dp[-1])[0]

def plan(T):
    W = find_oil(T)
    F = []
    n = len(W)
    count = 0
    for i in range(n):
        count += W[i]
    for i in range(n):
        if W[i] != 0 or i == n - 1:
            F.append(i)
    new_n = len(F)
    print(F)
    DP = [[inf for _ in range(count + 1)] for _ in range(new_n)]
    DP[0][W[0]] = 0
    for i in range(new_n):
        for j in range(count+1):
            if DP[i][j] != inf:
                k = i + 1
                while k < new_n and F[k] - F[i] <= j:
                    index = j - (F[k] - F[i]) + W[F[k]]
                    DP[k][index] = min(DP[k][index], DP[i][j] + 1)
                    k += 1
    return min(DP[new_n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

