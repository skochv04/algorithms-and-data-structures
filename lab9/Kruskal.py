#Wada: daje zbiór krawędzi, tworzące MST, ale bez drzewa
def Kruskal(G):
    n = len(G)
    T = []
    for i in range(n):
        for j, w in G[i]:
            T.append((w, i, j))
    T.sort()

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

    A = []

    for w, u, v in T:
        if findset(u) != findset(v):
            union(u, v)
            A.append((u, v, w))
    return A

# G = [[(1, 1), (4, 5), (5, 8)],
#      [(0, 1), (2, 3)],
#      [(1, 3), (3, 6), (4, 4)],
#      [(2, 6), (4, 2)],
#      [(0, 5), (2, 4), (3, 2), (5, 7)],
#      [(0, 8), (4, 7)]]

G = [
    [(1, 1), (2, 3), (3, 9), (4, 7), (5, 3), (6, 11)],
    [(0, 1), (2, 5)],
    [(0, 3), (1, 5)],
    [(0, 9), (4, 1)],
    [(0, 7), (3, 1), (5, 2)],
    [(0, 3), (4, 2), (6, 3)],
    [(0, 11), (5, 3)]
]

print(Kruskal(G))


