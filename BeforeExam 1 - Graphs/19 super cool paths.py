# We are given a weighted graph G. Super cool path is one that is not only the shortest weighted path
# between v and u, but also has the fewest edges (in other words we are looking for the shortest paths
# in terms of the number of edges among the shortest paths in the weight sense). Find algorithm that
# for a given starting vertex s will find super cool paths to other vertices.
from queue import PriorityQueue
inf = float('inf')

def relax(u, v, l, d, e, parent, q):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        parent[v] = u
        e[v] = e[u] + 1
        q.put((d[v], e[v], v))
    elif d[v] == d[u] + l:
        if e[v] > e[u] + 1:
            e[v] = e[u] + 1
            parent[v] = u
            q.put((d[v], e[v], v))

def super_cool_path(G, s):
    n = len(G)
    d = [inf for _ in range(n)]
    e = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    q = PriorityQueue()
    d[s] = 0
    e[s] = 0
    q.put((d[s], e[s], s))
    while not q.empty():
        du, ed, u = q.get()
        if d[u] == du:
            for v, l in G[u]:
                relax(u, v, l, d, e, parent, q)
    return d, e, parent



G = [[(1, 1), (5, 1), (7, 2)],
         [(0, 1), (2, 1)],
         [(1, 1), (3, 1)],
         [(2, 1), (4, 1)],
         [(3, 1), (6, 1), (7, 2)],
         [(0, 1), (6, 2)],
         [(5, 2), (4, 1)],
         [(0, 2), (4, 2)]]

print(super_cool_path(G, 0))