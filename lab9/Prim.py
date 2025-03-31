from queue import PriorityQueue

def relax(u, v, l, d, parent, queue):
    if d[v] > l:
        d[v] = l
        parent[v] = u
        queue.put((d[v], v, u))
    return

def Prim(G, s):
    n = len(G)
    d = [float('inf') for _ in range(n)]
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


G = [[(1, 1), (4, 5), (5, 8)],
     [(0, 1), (2, 3)],
     [(1, 3), (3, 6), (4, 4)],
     [(2, 6), (4, 2)],
     [(0, 5), (2, 4), (3, 2), (5, 7)],
     [(0, 8), (4, 7)]]

print(Prim(G, 2))
