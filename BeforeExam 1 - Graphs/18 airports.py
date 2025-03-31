# We are given a list of threes (city_A, city_B, cost). Each of them means that we can build a road
# between city_A and city_B for the given cost. Moreover in any city we can build an airport at a K cost,
# independent of the city. At the beginning, there is no airport in any city, nor is there a road built
# between any two cities. Our goal is to build airports and roads for a minimum total cost so that every
# city has access to the airport. The city has access to the airport if:
#   1) it has an airport
#   2) it is possible to travel to another city which has an airport
# If there is more than one solution with the minimum cost, choose the one with the most airports.

def make_graph(G):
    maxi = G[0][1]
    for i in G:
        maxi = max(maxi, i[1])
    M = [[] for _ in range(maxi + 1)]
    for u, v, w in G:
        M[u].append((v, w))
        M[v].append((u, w))
    return M

def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    def DFS_visit(G, u):
        visited[u] = True
        for v, l in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(G, v)

    connect = 0

    for u in range(len(G)):
        if not visited[u]:
            connect += 1
            DFS_visit(G, u)

    return connect

def Kruskal(G, K):
    n = G[0][1]
    T = []
    for i, j, w in G:
        T.append((w, i, j))
        n = max(n, j)
    T.sort()
    parent = [i for i in range(n+1)]
    rank = [0 for _ in range(n+1)]

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

    A = []
    for w, u, v in T:
        if findset(u) != findset(v) and w <= K:
            union(u, v)
            A.append((u, v, w))
    return A

def airports(G, K):
    sum = 0
    edges = Kruskal(G, K)
    for i in edges:
        sum += i[2]
    sum += DFS(make_graph(edges)) * K
    return sum

G = [(0, 1, 2), (0, 2, 3), (0, 6, 4), (0, 7, 7), (2, 3, 1), (2, 5, 5), (3, 4, 3),
         (6, 7, 4), (6, 8, 6), (7, 8, 2)]
K = 4
print(airports(G, K))