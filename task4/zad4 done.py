#Stas Kochevenko
#Opis: W danym algorytmie najpierw skorzystamy z BFSa, żeby znaleźć najkrótszą ścieżkę, wpisując krawędzi po których
#przechodzimy do tablicy. Jeśli ta ścieżka nie istnieje - zwrócamy None, jeśli istnieje - to dla każdej krawędzi z
#najkrótszej ścieźki uruchamiamy BFSa, który szuka takiej najkrótszej ścieżki, która nie zawiera tej krawędzi. Jeśli
#takiej ścieżki nie ma albo jest ona dłuższa od pierwszej, to zwracamy krawędź. Jeśli po wykonaniu pętli nie znalezliśmy
#takiej krawędzi, która spowoduje wydłużenie najkrótszej ścieżki między s a t, to zwracamy None.
#Złożoność obliczeniowa wynosi O((V + E) * E).

from zad4testy import runtests
from collections import deque
def BFS(G, x, y, v1 = -1, v2 = -1):
    q = deque()
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    q.append(x)
    visited[x] = True
    while len(q):
        u = q.popleft()
        for v in G[u]:
            if (u, v) != (v1, v2):
                if not visited[v]:
                    parent[v] = u
                    visited[v] = True
                    q.append(v)
    l = 1
    ind = y
    tab = []
    if parent[ind] != None:
        while (parent[ind] != x):
            tab.append((parent[ind], ind))
            l += 1
            ind = parent[ind]
        tab.append((parent[ind], ind))
        return l, tab
    return None

def longer( G, s, t ):
    b = BFS(G, s, t)
    if b != None:
        l = b[0]
        tab = b[1]
        for i in tab:
            k = BFS(G, s, t, i[0], i[1])
            if k == None or k[0] > l:
                return i
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )