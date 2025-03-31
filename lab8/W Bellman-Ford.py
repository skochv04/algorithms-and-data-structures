from math import inf

def relax(u, v, l, d, parent):
    if d[v] > d[u]+l:
        d[v] = d[u]+l
        parent[v] = u

def BellmanFord(G, s):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)] #długości najkrótszych ścieżek
    d[s] = 0
    for i in range(n - 1):
        for u in range(n):
            for v, l in G[u]:
                relax(u, v, l, d, parent)
    for u in range(n):
        for v, l in G[u]:
            if d[v] > d[u]+l:
                return None
    return d, parent



G = [[(1, 1), (8, 2)],
      [(0, 1), (2, 3), (6, 3)],
      [(1, 3), (3, 5)],
      [(2, 5), (4, 1), (6, 2)],
      [(3, 1), (5, 8), (7, 4)],
      [(4, 8), (6, 3), (7, 1)],
      [(1, 3), (3, 2), (5, 3), (8, 1)],
      [(4, 4), (5, 1), (8, 7)],
      [(6, 1), (7, 7), (0, 2)]]

print(BellmanFord(G, 0))