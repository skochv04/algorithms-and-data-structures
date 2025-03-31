from queue import PriorityQueue
inf = float('inf')

def relax(u, v, l, dist, parent, q, g):
    if dist[v] > dist[u] + l:
        dist[v] = dist[u] + l
        parent[v] = u
        q.put((dist[v], v, g-l))

def jak_dojade(G, P, d, a, b):
    n = len(G)
    parent = [None for _ in range(n)]
    dist = [inf for _ in range(n)]
    q = PriorityQueue()
    dist[a] = 0
    g = d
    q.put((dist[a], a, g))
    while not q.empty():
        du, u, g = q.get()
        if du == dist[u]:
            if u in P:
                g = d
            for v in range(n):
                l = G[u][v]
                if l > 0 and l <= g:
                    relax(u, v, l, dist, parent, q, g)
    if parent[b] != None:
        tab = []
        ind = b
        while ind != parent[a]:
            tab.append(ind)
            ind = parent[ind]
        tab=tab[::-1]
        return tab
    return None


G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
P = [0,1,3]

print(jak_dojade(G, P, 6, 1, 4))
#[0,3,2]