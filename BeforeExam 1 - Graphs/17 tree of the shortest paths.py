# We are given a weighted graph G and a spanning tree T that contains the vertex s. Find algorithm that
# checks if T is a tree of the shortest paths from the vertex s.

from queue import PriorityQueue
from math import inf

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
    d[s] = 0
    q.put((d[s], s))
    while not q.empty():
        du, u = q.get()
        if d[u] == du:
            for v, l in G[u]:
                relax(u, v, l, d, parent, q)
    return d


def tree_of_the_shortest_paths(G, T, s):
    d1 = Dijkstra(G, s)
    d2 = Dijkstra(T, s)
    n = len(G)
    for i in range(n):
        if d1[i] != d2[i]:
            return False
    return True



G = [
    [(1, 1), (2, 3), (3, 9), (4, 7), (5, 3), (6, 11)],
    [(0, 1), (2, 5)],
    [(0, 3), (1, 5)],
    [(0, 9), (4, 1)],
    [(0, 7), (3, 1), (5, 2)],
    [(0, 3), (4, 2), (6, 3)],
    [(0, 11), (5, 3)]
]

T = [
    [(1, 1), (2, 3), (5, 3)],
    [(0, 1)],
    [(0, 3)],
    [(4, 1)],
    [(3, 1), (5, 2)],
    [(0, 3), (4, 2), (6, 3)],
    [(5, 3)]
]

print(tree_of_the_shortest_paths(G, T, 0))