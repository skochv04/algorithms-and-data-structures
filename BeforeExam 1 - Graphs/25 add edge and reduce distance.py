# We are given a weighted graph G with positive weights. There is also given a list of edges E' that
# do not belong to the graph, but they are edges between the vertices in G. The two vertices s and t
# are also given. Determine which edge from E' should be added to the graph G to reduce the distance
# between s and t as much as possible. If neither edge lower the distance between s and t, the
# algorithm should return False.

from queue import PriorityQueue
inf = float('inf')

def relax(u, v, l, d, parent, queue):
    if d[v] > d[u]+l:
        d[v] = d[u]+l
        parent[v] = u
        queue.put((d[v], v))

def Dijkstry(G, s, t):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)] #długości najkrótszych ścieżek
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s], s))
    while not q.empty():
        du, u = q.get()
        if d[u] == du:
            for v in range(n):
                l = G[u][v]
                if l != 0:
                    relax(u, v, l, d, parent, q)
    return d

def add_edge_reduce_distance(G, E, s, t):
    # path = Dijkstry(G, s, t)
    # mini_path = path
    # edge = False
    # for u, v, l in E:
    #     G[u][v] = l
    #     G[v][u] = l
    #     P = Dijkstry(G, s, t)
    #     if P < mini_path:
    #         mini_path = P
    #         edge = ((u, v))
    #     G[u][v] = 0
    #     G[v][u] = 0
    d1 = Dijkstry(G, s, t)
    d2 = Dijkstry(G, t, s)
    res = None
    dist = d1[t]
    for u, v, l in E:
        if d1[u] + l + d2[v] < dist:
            res = (u, v)
            dist = d1[u] + l + d2[v]
    return res

G =     [[0, 0, 1, 2, 0, 0, 0, 0],
         [0, 0, 0, 0, 5, 0, 0, 0],
         [1, 0, 0, 6, 4, 8, 0, 0],
         [2, 0, 6, 0, 0, 0, 0, 0],
         [0, 5, 4, 0, 0, 0, 0, 6],
         [0, 0, 8, 0, 0, 0, 4, 1],
         [0, 0, 0, 0, 0, 4, 0, 7],
         [0, 0, 0, 0, 6, 1, 7, 0]]

E = [(0, 1, 3), (3, 5, 5), (3, 6, 6), (4, 5, 3)]
print(add_edge_reduce_distance(G, E, 0, len(G)-1))