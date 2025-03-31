# Chouti was tired of the tedious homework, so he opened up an old programming problem he created
# years ago. You are given a connected undirected graph with n vertices and m weighted edges. There
# are k special vertices: x1, x2, ..., xk. Let's define the cost of the path as the maximum weight of
# the edges in it. And the distance between two vertexes as the minimum cost of the paths connecting
# them. For each special vertex, find another special vertex which is farthest from it (in terms of
# the previous paragraph, i.e. the corresponding distance is maximum possible) and output the
# distance between them.

def Kruskal(edges, visited):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    rank = [0 for _ in range(n + 1)]

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

    for u, v, w in edges:
        if findset(u) != findset(v):
            union(u, v)
            if visited[v]:
                A.append((u, v, w))
    return A

def maximum_distance(n, k, special, edges):
    visited = [False for _ in range(n + 1)]
    for i in special:
        visited[i] = True
    path = Kruskal(edges, visited)
    path.sort(key=lambda x: x[2])
    return path[-1][2]

n = 5
k = 4
special = [1, 2, 3, 4]
edges = [(1, 5, 4), (1, 3, 3), (2, 4, 4), (2, 5, 6), (3, 4, 3)]
print(maximum_distance(n, k, special, edges))