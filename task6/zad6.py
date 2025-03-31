#Stas Kochevenko
#Opis: Zadanie polega na znalezieniu największej możliwej ilości skojarzeń w grafie dwudzielnym, więc na początku
#przetwarzamy tablicę wejściową, zwiększając każdy element o rozmiar tablicy. Będziemy mieli "dwa zbiory" grafa
#dwudzielnego, czyli z indeksami od 0 ... n-1 oraz n, ... n*2 - 1. Dla rozwiązania zadania skorzystamy z algorytmu
#Hopcrofta-Karpa. Tworzymy zmienną wyniku równą 0, tablicę odległości oraz tablicę par, gdzie na początku wszystkie
#wierszchołki mają wartość PAR (czyli ich para to fikcyjny wierszchołek s/t). Następnie, dopóki algorytm BFS znajduję
#dowolną ścieżkę powiększającą z lewego zbioru do prawego, dla każdego wierszchołka z lewego zbioru, jeśli jego para to
#PAR i DFS znajduję ścieżkę powiększającą, aktualizując pair, zwiększamy wynik o 1. Po wykonaniu pętli zwrócamy wynik.
#Złożoność obliczeniowa tego algorytmu wynosi O(E sqrt(V)).

from zad6testy import runtests
from collections import deque

INF = float('inf')
PAR = -1

def make_list(M):
    n = len(M)
    for i in range(n):
        for j in range(len(M[i])):
            M[i][j] += n
    return M

def BFS(G, m, d, pair):
    q = deque()
    for u in range(m):
        if pair[u] == PAR:
            d[u] = 0
            q.append(u)
        else:
            d[u] = INF
    d[PAR] = INF
    while len(q):
        u = q.popleft()
        if d[u] < d[PAR]:
            for v in G[u]:
                if d[pair[v]] == INF:
                    d[pair[v]] = d[u] + 1
                    q.append(pair[v])
    return d[PAR] != INF

def DFS(G, u, d, pair):
    if u!= PAR:
        for v in G[u]:
            if d[pair[v]] == d[u] + 1:
                if DFS(G, pair[v], d, pair):
                    pair[v] = u
                    pair[u] = v
                    return True
        d[u] = INF
        return False
    return True

def binworker( M ):
    n = len(M)
    M = make_list(M)
    pair = [PAR for _ in range(n*2)]
    d = [0 for _ in range(n*2)]
    count = 0
    path = BFS(M, n, d, pair)
    while path:
        for u in range(n):
            if pair[u] == PAR and DFS(M, u, d, pair):
                count += 1
        path = BFS(M, n, d, pair)
    return count

M = [[0, 1, 3], [2, 4], [0, 2], [3], [3, 2]]
print(binworker(M))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )