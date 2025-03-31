# Mahmoud and Ehab continue their adventures! As everybody in the evil land knows, Dr. Evil likes
# bipartite graphs, especially trees. A tree is a connected acyclic graph. A bipartite graph is a graph,
# whose vertices can be partitioned into 2 sets in such a way, that for each edge (u, v) that belongs
# to the graph, u and v belong to different sets. Dr. Evil gave Mahmoud and Ehab a tree consisting of
# n nodes and asked them to add edges to it in such a way, that the graph is still bipartite. Besides,
# after adding these edges the graph should be simple (doesn't contain loops or multiple edges).
# What is the maximum number of edges they can add?

from collections import deque

def make_graph(edges):
    n = len(edges)
    max_vertex = 0
    for i in range(n):
        max_vertex = max(max_vertex, max(edges[i]))
    G = [[0 for _ in range(max_vertex + 1)] for _ in range(max_vertex + 1)]
    for i in range(n):
        G[edges[i][0]][edges[i][1]] = 1
        G[edges[i][1]][edges[i][0]] = 1
    return G

def add_edges(n, T):
    G = make_graph(T)
    q = deque()
    n = len(G)
    visited = [False for _ in range(n)]
    odd = [-1 for _ in range(n)]
    odd[0] = None
    q.append(1)
    visited[1] = True
    odd[1] = 0
    while len(q):
        u = q.popleft()
        for v in range(n):
            if G[u][v]:
                if not visited[v]:
                    visited[v] = True
                    odd[v] = 1 - odd[u]  # zamieniamy 1 na 0 oraz 0 na 1
                    q.append(v)
                elif odd[v] == odd[u]:
                    return False
    q = 0

    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    def findset(x):
        if parent[x] != x:
            parent[x] = findset(parent[x])
        return parent[x]

    def union(x, y):
        x, y = findset(x), findset(y)
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1
    T.sort(reverse=True)
    for u, v in T:
        union(u, v)

    for u in range(1, n):
        for v in range(1, n):
            if not G[u][v] and odd[v] != odd[u] and findset(u) == findset(v):
                G[u][v] = 1
                G[v][u] = 1
                q += 1
                union(u, v)
    return q


n = 10
T = [(7, 6), (2, 7), (4, 1), (8, 5), (9, 4), (5, 3), (8, 7), (0, 8), (0, 4)]
print(add_edges(n, T))