#Stas Kochevenko
#Opis: Najpierw przygotowujemy dane z tablic E oraz S, umieszczając je liniowo w nowej tablicy G - reprezentacji całego
#grafu jako listę sąsiedztwa. Wierzchołki z tablicy S będą miały krawędzi między sobą z zerowym kosztem przejścia.
#Następnie główna funkcja zwraca wynik działania algorytmu Dijkstry. Ten algorytm szuka najkrótszej ścieżki w grafie
#ważonym od a do b, a po wykonaniu tego zwraca czas tej podróży, jeśli ścieżka istnieje, i None jeśli nie istnieje.
#Złożonożść tego algorytmu to O(E + S + E log V).

from zad5testy import runtests
from queue import PriorityQueue

def relax(u, v, l, d, parent, queue):
    if d[v] > d[u]+l:
        d[v] = d[u]+l
        parent[v] = u
        queue.put((d[v], v))

def Dijkstry(G, a, b):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    q = PriorityQueue()
    d[a] = 0
    q.put((d[a], a))
    while not q.empty():
        du, u = q.get()
        if d[u] == du:
            for v, l in G[u]:
                relax(u, v, l, d, parent, q)
    if d[b] != float('inf'):
        return d[b]
    return None

def spacetravel( n, E, S, a, b ):
    G = [[] for _ in range(n)]
    for v, u, koszt in E:
        G[v].append((u, koszt))
        G[u].append((v, koszt))
    for i in range(len(S)-1):
        G[S[i]].append((S[i+1], 0))
        G[S[i+1]].append((S[i], 0))
    G[S[0]].append((S[-1], 0))
    G[S[-1]].append((S[0], 0))
    return Dijkstry(G, a, b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )