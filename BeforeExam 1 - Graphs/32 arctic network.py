# In the Arctic, settlements are very distant from each other. We are given them as pairs of
# coordinates (x, y). Some of them have satellite receivers - from such a settlement you can
# directly communicate with any other settlement that has a satellite receiver. We now want to
# place radio receivers with the same limited range D (integer) in every settlement, so that we
# can communicate (directly or indirectly) between each pair of settlements. Find the minimum D.
from math import ceil
from math import sqrt
from queue import PriorityQueue

inf = float('inf')

def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return ceil(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

def relax(u, v, l, d, parent, queue):
    if d[v] > l:
        d[v] = l
        parent[v] = u
        queue.put((d[v], v, u))

def Prim(G, s, receivers):
    n = len(G)
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    MST = []
    q = PriorityQueue()

    d[s] = 0
    q.put((d[s], s, s))

    while not q.empty():
        du, u, w = q.get()
        if not visited[u] and du == d[u]:
            visited[u] = True
            MST.append((w, u, du))
            for v, l in G[u]:
                if not visited[v]:
                    relax(u, v, l, d, parent, q)
    MST.pop(0)
    return MST

def arctic_network(settlments, receivers):
    n = len(settlments)
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d = distance(settlments[i], settlments[j])
            G[i].append((j, d))
            G[j].append((i, d))
    i = j = 0
    tab = [-1 for _ in range(len(receivers))]
    while i < n and j < len(receivers):
        s, t = settlments[i], receivers[j]
        if s == t:
            tab[j] = i
            j += 1
        i += 1
    for i in range(len(tab)):
        for j in range(i+1, len(tab)):
            G[tab[i]][tab[j]] = ((tab[j], 0))
            G[tab[j]][tab[i]] = ((tab[i], 0))

    MST = Prim(G, 0, receivers)
    dist = 0
    print(MST)
    for i in MST:
        dist = max(dist, i[2])
    return dist

settlments = [(1, 1), (2, 3), (-5, 1), (-3, 1), (-2, -2), (-2, 1), (6, 4), (5, 2), (-3, -3), (-5, 4)]
receivers = [(-3, 1), (-2, 1), (5, 2)]
print(arctic_network(settlments, receivers))