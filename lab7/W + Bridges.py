inf = float("inf")
def find_bridges(G):
    n = len(G)
    d = [inf for _ in range(n)]
    low = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    def DFS_visit(G, u):
        nonlocal time
        visited[u] = True
        d[u] = time
        low[u] = time
        time += 1
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(G, v)
                low[u] = min(low[u], low[v])
                # if low[v] > d[u]:
                #     tab.append((u, v))
            elif v != parent[u]: #krawędż wstęczna
                low[u] = min(low[u], d[v])

    time = 0
    tab = []
    for u in range(n):
        if not visited[u]:
            DFS_visit(G, u)
    for i in range(n):
        if d[i] == low[i] and parent[i] is not None:
            tab.append((parent[i], i))
    return tab


G = [[1, 6],
     [0, 2],
     [1, 3, 6],
     [2, 4, 5],
     [3, 5],
     [3, 4],
     [0, 2, 7],
     [6]]

print(find_bridges(G))