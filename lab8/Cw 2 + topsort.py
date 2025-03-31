#Wyszukujemy ścieżek do wszystkich wierszchołków grafu acycklicznego skierowanego O(E)
from math import inf

def topsort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    def DFS_visit(G, u):
        nonlocal time
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v[0]]:
                parent[v[0]] = u
                DFS_visit(G, v[0])
        time += 1
        tab.append(u)

    time = 0
    tab = []
    for u in range(len(G)):
        if not visited[u]:
            DFS_visit(G, u)
    return tab[::-1]

def relax(u, v, l, d, parent):
    if d[v] > d[u]+l:
        d[v] = d[u]+l
        parent[v] = u

def find_paths(G, s):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    T = topsort(G)
    d[s] = 0
    for u in range(T.index(s), n):
        for v, l in G[T[u]]:
            relax(T[u], v, l, d, parent)
    return d, parent

# G = [[1],
#      [3],
#      [],
#      [2]]

G = [[(1, 34), (6, 7)],
     [(2, 29), (6, 18)],
     [(3, 11), (4, 35)],
     [],
     [],
     [(2, 0)],
     []]
#
# for i in range(len(G)):
#     print(i, G[i])
print(find_paths(G, 2))