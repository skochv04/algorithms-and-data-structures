from queue import PriorityQueue

def add_edges(u, G, mst, visited, q):
    for v, w in G[u]:
        if not visited[v]:
            q.put((w, u, v))

def prim_mst(G):
    s = 2
    n = len(G)
    visited = [False for _ in range(n)]
    mst = []
    q = PriorityQueue()
    q.put((0, s, s))
    while len(mst) < n:
        w, u, v = q.get()
        if not visited[v]:
            visited[v] = True
            mst.append((u, v, w))
            add_edges(v, G, mst, visited, q)
            for i, w in G[v]:
                if not visited[i]:
                    q.put((w, v, i))

    return mst[1:]

G = [[(1, 1), (4, 5), (5, 8)],
     [(0, 1), (2, 3)],
     [(1, 3), (3, 6), (4, 4)],
     [(2, 6), (4, 2)],
     [(0, 5), (2, 4), (3, 2), (5, 7)],
     [(0, 8), (4, 7)]]

print(prim_mst(G))