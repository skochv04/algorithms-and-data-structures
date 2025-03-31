def Floyd_Warshall(G):
    n = len(G)
    d = [[float("inf") for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if G[u][v]:
                d[u][v] = G[u][v]
        d[u][u] = 0
    for t in range(n):
        for u in range(n):
            for v in range(n):
                d[u][v] = min(d[u][v], d[u][t]+d[t][v])
    return d

# G = [[0, 25, 16, 0],
#      [25, 0, 0, 4],
#      [16, 0, 0, 1],
#      [0, 4, 1, 0]]

G =     [[0, 2, 0, 1, 0, 0, 3],
         [2, 0, 0, 1, 2, 2, 0],
         [0, 0, 0, 1, 1, 0, 5],
         [1, 1, 1, 0, 0, 4, 0],
         [0, 2, 1, 0, 0, 0, 0],
         [0, 2, 0, 4, 0, 0, 0],
         [3, 0, 5, 0, 0, 0, 0]]
n = len(G)

A = Floyd_Warshall(G)

for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()
