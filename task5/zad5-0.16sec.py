#Stas Kochevenko
#Opis:

from zad5testy import runtests
from queue import PriorityQueue

def relax(u, v, l, d, parent, queue):
    if d[v] > d[u]+l:
        d[v] = d[u]+l
        parent[v] = u
        queue.put((d[v], v))

def Dijkstra(G, a, b, S):
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
            if u in S:
                for j in S:
                    relax(u, j, 0, d, parent, q)

    if d[b] != float('inf'):
        return d[b]
    return None

def spacetravel( n, E, S, a, b ):
    G = [[] for _ in range(n)]
    for v, u, koszt in E:
        G[v].append((u, koszt))
        G[u].append((v, koszt))
    return Dijkstra(G, a, b, S)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )