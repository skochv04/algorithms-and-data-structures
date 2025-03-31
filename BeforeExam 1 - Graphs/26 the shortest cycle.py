# We are given a weighted graph with positive weights. Find the length of the shortest cycle in graph.
# Algorithm should return False if there is no cycle.

from queue import PriorityQueue
inf = float('inf')

def relax(u, v, l, d, parent, q):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        parent[v] = u
        q.put((d[v], v))

def Dijkstry(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s], s))
    minimal_cycle = inf
    while not q.empty():
        du, u = q.get()
        visited[u] = True
        for v in range(n):
            l = G[u][v]
            if l != 0:
                relax(u, v, l, d, parent, q)
                if v != parent[u] and visited[v]:
                    minimal_cycle = min(minimal_cycle, d[v] + l + d[u])
    return minimal_cycle

def the_shortest_cycle(G):
    n = len(G)
    minimal_d = inf
    for i in range(n):
        minimal_d = min(minimal_d, Dijkstry(G, i))
    return minimal_d

G =     [[0, 0, 1, 2, 0, 0, 0, 0],
         [0, 0, 0, 0, 5, 0, 0, 0],
         [1, 0, 0, 6, 4, 8, 0, 0],
         [2, 0, 6, 0, 0, 0, 0, 0],
         [0, 5, 4, 0, 0, 0, 0, 6],
         [0, 0, 8, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 4, 0, 7],
         [0, 0, 0, 0, 6, 1, 7, 0]]

print(the_shortest_cycle(G))