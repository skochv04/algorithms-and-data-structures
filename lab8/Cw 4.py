#Szukamy najkrótszej ścieżki, ale nie sumy, a iloczynu wag
#log(a * b * c) = log(a) + log(b) + log(c)
from math import log
from queue import PriorityQueue
from math import inf

def relax(u, v, l, d, parent, queue):
    if d[v] > d[u]+l:
        d[v] = d[u]+l
        parent[v] = u
        queue.put((d[v], v))

def Dijkstra(G, s):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)] #długości najkrótszych ścieżek
    q = PriorityQueue()
    d[s] = 1
    q.put((d[s], s))
    while not q.empty():
        du, u = q.get()
        if d[u] == du:
            for v, l in G[u]:
                l = log(l, 2)
                relax(u, v, l, d, parent, q)
    return parent

def print_path(start, v, parent):
    path = [v]
    while v != start:
        v = parent[v]
        path.append(v)
    for i in range(len(path)-1, -1, -1):
        print(path[i], end=" ")

G = [[(1, 1), (8, 2)],
      [(0, 1), (2, 3), (6, 3)],
      [(1, 3), (3, 5)],
      [(2, 5), (4, 1), (6, 2)],
      [(3, 1), (5, 8), (7, 4)],
      [(4, 8), (6, 3), (7, 1)],
      [(1, 3), (3, 2), (5, 3), (8, 1)],
      [(4, 4), (5, 1), (8, 7)],
      [(6, 1), (7, 7), (0, 2)]]

parent = Dijkstra(G, 1)
print_path(1, 3, parent)
